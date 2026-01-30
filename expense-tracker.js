// Expense Tracker JavaScript Application
// This demonstrates CRUD operations, data validation, filtering, and local JSON database simulation

/**
 * Data Management Module
 * Simulates a local JSON database using localStorage
 */
class ExpenseDatabase {
    constructor() {
        this.storageKey = 'expenseTrackerData';
        this.initializeDatabase();
    }
    
    // Initialize database with sample data if empty
    initializeDatabase() {
        if (!localStorage.getItem(this.storageKey)) {
            const sampleData = {
                expenses: [
                    {
                        id: 1,
                        amount: 25.50,
                        category: 'food',
                        date: '2024-01-15',
                        description: 'Lunch at cafe',
                        createdAt: new Date().toISOString()
                    },
                    {
                        id: 2,
                        amount: 60.00,
                        category: 'transport',
                        date: '2024-01-14',
                        description: 'Gas for car',
                        createdAt: new Date().toISOString()
                    },
                    {
                        id: 3,
                        amount: 15.99,
                        category: 'entertainment',
                        date: '2024-01-13',
                        description: 'Movie ticket',
                        createdAt: new Date().toISOString()
                    }
                ],
                nextId: 4,
                lastModified: new Date().toISOString()
            };
            this.saveData(sampleData);
        }
    }
    
    // Load all data from localStorage (simulates reading JSON file)
    loadData() {
        try {
            const data = localStorage.getItem(this.storageKey);
            return data ? JSON.parse(data) : { expenses: [], nextId: 1 };
        } catch (error) {
            console.error('Error loading data from localStorage:', error);
            return { expenses: [], nextId: 1 };
        }
    }
    
    // Save data to localStorage (simulates writing to JSON file)
    saveData(data) {
        try {
            data.lastModified = new Date().toISOString();
            localStorage.setItem(this.storageKey, JSON.stringify(data));
            return true;
        } catch (error) {
            console.error('Error saving data to localStorage:', error);
            return false;
        }
    }
    
    // CRUD Operations
    
    // CREATE: Add new expense
    addExpense(expenseData) {
        const data = this.loadData();
        const newExpense = {
            id: data.nextId,
            amount: parseFloat(expenseData.amount),
            category: expenseData.category,
            date: expenseData.date,
            description: expenseData.description || '',
            createdAt: new Date().toISOString()
        };
        
        data.expenses.push(newExpense);
        data.nextId++;
        
        if (this.saveData(data)) {
            return newExpense;
        }
        return null;
    }
    
    // READ: Get all expenses
    getAllExpenses() {
        return this.loadData().expenses;
    }
    
    // READ: Get expense by ID
    getExpenseById(id) {
        const data = this.loadData();
        return data.expenses.find(expense => expense.id === parseInt(id));
    }
    
    // UPDATE: Modify existing expense
    updateExpense(id, updatedData) {
        const data = this.loadData();
        const index = data.expenses.findIndex(expense => expense.id === parseInt(id));
        
        if (index !== -1) {
            data.expenses[index] = {
                ...data.expenses[index],
                amount: parseFloat(updatedData.amount),
                category: updatedData.category,
                date: updatedData.date,
                description: updatedData.description || '',
                updatedAt: new Date().toISOString()
            };
            
            if (this.saveData(data)) {
                return data.expenses[index];
            }
        }
        return null;
    }
    
    // DELETE: Remove expense
    deleteExpense(id) {
        const data = this.loadData();
        const index = data.expenses.findIndex(expense => expense.id === parseInt(id));
        
        if (index !== -1) {
            const deletedExpense = data.expenses.splice(index, 1)[0];
            if (this.saveData(data)) {
                return deletedExpense;
            }
        }
        return null;
    }
    
    // Get expenses with filtering and sorting
    getFilteredExpenses(filters = {}) {
        let expenses = this.getAllExpenses();
        
        // Filter by category
        if (filters.category && filters.category !== '') {
            expenses = expenses.filter(expense => expense.category === filters.category);
        }
        
        // Filter by month
        if (filters.month && filters.month !== '') {
            expenses = expenses.filter(expense => expense.date.startsWith(filters.month));
        }
        
        // Filter by date range
        if (filters.startDate) {
            expenses = expenses.filter(expense => expense.date >= filters.startDate);
        }
        if (filters.endDate) {
            expenses = expenses.filter(expense => expense.date <= filters.endDate);
        }
        
        // Sort expenses
        if (filters.sortBy) {
            expenses = this.sortExpenses(expenses, filters.sortBy);
        }
        
        return expenses;
    }
    
    // Sort expenses by different criteria
    sortExpenses(expenses, sortBy) {
        return expenses.sort((a, b) => {
            switch (sortBy) {
                case 'date-desc':
                    return new Date(b.date) - new Date(a.date);
                case 'date-asc':
                    return new Date(a.date) - new Date(b.date);
                case 'amount-desc':
                    return b.amount - a.amount;
                case 'amount-asc':
                    return a.amount - b.amount;
                default:
                    return new Date(b.date) - new Date(a.date);
            }
        });
    }
}

/**
 * Validation Module
 */
class ExpenseValidator {
    static validateExpense(data) {
        const errors = [];
        
        // Validate amount
        if (!data.amount || parseFloat(data.amount) <= 0) {
            errors.push('Amount must be a positive number');
        }
        
        // Validate category
        if (!data.category || data.category.trim() === '') {
            errors.push('Category is required');
        }
        
        // Validate date
        if (!data.date) {
            errors.push('Date is required');
        } else {
            const expenseDate = new Date(data.date);
            const today = new Date();
            if (expenseDate > today) {
                errors.push('Date cannot be in the future');
            }
        }
        
        return {
            isValid: errors.length === 0,
            errors
        };
    }
}

/**
 * UI Manager Class
 */
class ExpenseTracker {
    constructor() {
        this.db = new ExpenseDatabase();
        this.categoryChart = null;
        this.monthlyChart = null;
        this.currentFilters = {};
        
        this.init();
    }
    
    init() {
        this.setupEventListeners();
        this.setDefaultDate();
        this.refreshUI();
        this.initializeCharts();
        
        console.log('💰 Expense Tracker Loaded Successfully!');
        console.log('📊 Features: CRUD operations, filtering, charts, data export');
        console.log('💾 Using localStorage to simulate JSON database');
    }
    
    setupEventListeners() {
        // Form submission
        document.getElementById('expenseForm').addEventListener('submit', (e) => {
            e.preventDefault();
            this.addExpense();
        });
        
        // Edit form submission
        document.getElementById('editForm').addEventListener('submit', (e) => {
            e.preventDefault();
            this.updateExpense();
        });
        
        // Filter change events
        document.getElementById('filterCategory').addEventListener('change', () => {
            this.applyFilters();
        });
        
        document.getElementById('filterMonth').addEventListener('change', () => {
            this.applyFilters();
        });
        
        document.getElementById('sortBy').addEventListener('change', () => {
            this.applyFilters();
        });
        
        // Modal events
        document.querySelector('.close').addEventListener('click', () => {
            this.closeModal();
        });
        
        document.querySelector('.btn-cancel').addEventListener('click', () => {
            this.closeModal();
        });
        
        // Close modal when clicking outside
        window.addEventListener('click', (e) => {
            const modal = document.getElementById('editModal');
            if (e.target === modal) {
                this.closeModal();
            }
        });
    }
    
    setDefaultDate() {
        const today = new Date().toISOString().split('T')[0];
        document.getElementById('date').value = today;
    }
    
    // Add new expense (CREATE operation)
    addExpense() {
        const formData = new FormData(document.getElementById('expenseForm'));
        const expenseData = Object.fromEntries(formData);
        
        // Validate input
        const validation = ExpenseValidator.validateExpense(expenseData);
        if (!validation.isValid) {
            this.showMessage(validation.errors.join(', '), 'error');
            return;
        }
        
        // Add to database
        const newExpense = this.db.addExpense(expenseData);
        if (newExpense) {
            this.showMessage('Expense added successfully!', 'success');
            document.getElementById('expenseForm').reset();
            this.setDefaultDate();
            this.refreshUI();
        } else {
            this.showMessage('Error adding expense. Please try again.', 'error');
        }
    }
    
    // Edit expense (UPDATE operation)
    editExpense(id) {
        const expense = this.db.getExpenseById(id);
        if (!expense) {
            this.showMessage('Expense not found.', 'error');
            return;
        }
        
        // Populate edit form
        document.getElementById('editId').value = expense.id;
        document.getElementById('editAmount').value = expense.amount;
        document.getElementById('editCategory').value = expense.category;
        document.getElementById('editDate').value = expense.date;
        document.getElementById('editDescription').value = expense.description;
        
        // Show modal
        document.getElementById('editModal').style.display = 'block';
    }
    
    updateExpense() {
        const formData = new FormData(document.getElementById('editForm'));
        const expenseData = Object.fromEntries(formData);
        
        // Validate input
        const validation = ExpenseValidator.validateExpense(expenseData);
        if (!validation.isValid) {
            this.showMessage(validation.errors.join(', '), 'error');
            return;
        }
        
        // Update in database
        const updatedExpense = this.db.updateExpense(expenseData.id, expenseData);
        if (updatedExpense) {
            this.showMessage('Expense updated successfully!', 'success');
            this.closeModal();
            this.refreshUI();
        } else {
            this.showMessage('Error updating expense. Please try again.', 'error');
        }
    }
    
    // Delete expense (DELETE operation)
    deleteExpense(id) {
        if (!confirm('Are you sure you want to delete this expense?')) {
            return;
        }
        
        const deletedExpense = this.db.deleteExpense(id);
        if (deletedExpense) {
            this.showMessage('Expense deleted successfully!', 'success');
            this.refreshUI();
        } else {
            this.showMessage('Error deleting expense. Please try again.', 'error');
        }
    }
    
    // Apply filters and refresh display
    applyFilters() {
        this.currentFilters = {
            category: document.getElementById('filterCategory').value,
            month: document.getElementById('filterMonth').value,
            sortBy: document.getElementById('sortBy').value
        };
        
        this.displayExpenses();
        this.updateCharts();
    }
    
    // Clear all filters
    clearFilters() {
        document.getElementById('filterCategory').value = '';
        document.getElementById('filterMonth').value = '';
        document.getElementById('sortBy').value = 'date-desc';
        
        this.currentFilters = {};
        this.displayExpenses();
        this.updateCharts();
    }
    
    // Refresh entire UI
    refreshUI() {
        this.updateSummaryCards();
        this.displayExpenses();
        this.updateCharts();
    }
    
    // Update summary cards
    updateSummaryCards() {
        const expenses = this.db.getAllExpenses();
        const currentMonth = new Date().toISOString().slice(0, 7);
        
        // Calculate totals
        const totalAmount = expenses.reduce((sum, expense) => sum + expense.amount, 0);
        const monthlyAmount = expenses
            .filter(expense => expense.date.startsWith(currentMonth))
            .reduce((sum, expense) => sum + expense.amount, 0);
        const transactionCount = expenses.length;
        
        // Update UI
        document.getElementById('totalAmount').textContent = `$${totalAmount.toFixed(2)}`;
        document.getElementById('monthlyAmount').textContent = `$${monthlyAmount.toFixed(2)}`;
        document.getElementById('transactionCount').textContent = transactionCount;
    }
    
    // Display expenses list
    displayExpenses() {
        const filteredExpenses = this.db.getFilteredExpenses(this.currentFilters);
        const expensesList = document.getElementById('expensesList');
        
        if (filteredExpenses.length === 0) {
            expensesList.innerHTML = `
                <div class="no-expenses fade-in">
                    <i class="fas fa-inbox"></i>
                    <p>No expenses found matching your criteria.</p>
                </div>
            `;
            return;
        }
        
        const expensesHTML = filteredExpenses.map(expense => `
            <div class="expense-item slide-up" data-id="${expense.id}">
                <div class="expense-details">
                    <h4>
                        <span class="category-icon category-${expense.category}">
                            ${this.getCategoryIcon(expense.category)}
                        </span>
                        ${this.getCategoryName(expense.category)}
                    </h4>
                    <p><i class="fas fa-calendar"></i> ${this.formatDate(expense.date)}</p>
                    <p><i class="fas fa-comment"></i> ${expense.description || 'No description'}</p>
                </div>
                <div class="expense-amount">$${expense.amount.toFixed(2)}</div>
                <div class="expense-actions">
                    <button class="btn-edit" onclick="expenseTracker.editExpense(${expense.id})" title="Edit">
                        <i class="fas fa-edit"></i>
                    </button>
                    <button class="btn-delete" onclick="expenseTracker.deleteExpense(${expense.id})" title="Delete">
                        <i class="fas fa-trash"></i>
                    </button>
                </div>
            </div>
        `).join('');
        
        expensesList.innerHTML = expensesHTML;
    }
    
    // Initialize charts
    initializeCharts() {
        const categoryCtx = document.getElementById('categoryChart').getContext('2d');
        const monthlyCtx = document.getElementById('monthlyChart').getContext('2d');
        
        // Category Chart (Pie Chart)
        this.categoryChart = new Chart(categoryCtx, {
            type: 'pie',
            data: {
                labels: [],
                datasets: [{
                    data: [],
                    backgroundColor: [
                        '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0',
                        '#9966FF', '#FF9F40', '#FF6384', '#C9CBCF'
                    ]
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'bottom'
                    }
                }
            }
        });
        
        // Monthly Chart (Line Chart)
        this.monthlyChart = new Chart(monthlyCtx, {
            type: 'line',
            data: {
                labels: [],
                datasets: [{
                    label: 'Monthly Expenses',
                    data: [],
                    borderColor: '#667eea',
                    backgroundColor: 'rgba(102, 126, 234, 0.1)',
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: {
                            callback: function(value) {
                                return '$' + value;
                            }
                        }
                    }
                }
            }
        });
        
        this.updateCharts();
    }
    
    // Update charts with current data
    updateCharts() {
        const expenses = this.db.getFilteredExpenses(this.currentFilters);
        
        // Update Category Chart
        const categoryData = this.getCategoryData(expenses);
        this.categoryChart.data.labels = categoryData.labels;
        this.categoryChart.data.datasets[0].data = categoryData.data;
        this.categoryChart.update();
        
        // Update Monthly Chart
        const monthlyData = this.getMonthlyData(expenses);
        this.monthlyChart.data.labels = monthlyData.labels;
        this.monthlyChart.data.datasets[0].data = monthlyData.data;
        this.monthlyChart.update();
    }
    
    // Get category breakdown data
    getCategoryData(expenses) {
        const categoryTotals = {};
        
        expenses.forEach(expense => {
            if (!categoryTotals[expense.category]) {
                categoryTotals[expense.category] = 0;
            }
            categoryTotals[expense.category] += expense.amount;
        });
        
        return {
            labels: Object.keys(categoryTotals).map(cat => this.getCategoryName(cat)),
            data: Object.values(categoryTotals)
        };
    }
    
    // Get monthly trend data
    getMonthlyData(expenses) {
        const monthlyTotals = {};
        
        expenses.forEach(expense => {
            const month = expense.date.slice(0, 7); // YYYY-MM
            if (!monthlyTotals[month]) {
                monthlyTotals[month] = 0;
            }
            monthlyTotals[month] += expense.amount;
        });
        
        const sortedMonths = Object.keys(monthlyTotals).sort();
        
        return {
            labels: sortedMonths.map(month => this.formatMonth(month)),
            data: sortedMonths.map(month => monthlyTotals[month])
        };
    }
    
    // Export data to JSON file
    exportData() {
        const data = this.db.loadData();
        const exportData = {
            ...data,
            exportedAt: new Date().toISOString(),
            totalExpenses: data.expenses.length,
            totalAmount: data.expenses.reduce((sum, expense) => sum + expense.amount, 0)
        };
        
        const dataStr = JSON.stringify(exportData, null, 2);
        const dataBlob = new Blob([dataStr], { type: 'application/json' });
        const url = URL.createObjectURL(dataBlob);
        
        const link = document.createElement('a');
        link.href = url;
        link.download = `expense-tracker-export-${new Date().toISOString().slice(0, 10)}.json`;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        URL.revokeObjectURL(url);
        
        this.showMessage('Data exported successfully!', 'success');
        
        console.log('📋 Export Data:', exportData);
    }
    
    // Utility functions
    getCategoryIcon(category) {
        const icons = {
            food: '🍕',
            transport: '🚗',
            entertainment: '🎬',
            shopping: '🛍️',
            utilities: '⚡',
            healthcare: '🏥',
            education: '📚',
            travel: '✈️',
            other: '🔗'
        };
        return icons[category] || '📝';
    }
    
    getCategoryName(category) {
        const names = {
            food: 'Food & Dining',
            transport: 'Transportation',
            entertainment: 'Entertainment',
            shopping: 'Shopping',
            utilities: 'Utilities',
            healthcare: 'Healthcare',
            education: 'Education',
            travel: 'Travel',
            other: 'Other'
        };
        return names[category] || 'Unknown';
    }
    
    formatDate(dateStr) {
        return new Date(dateStr).toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'short',
            day: 'numeric'
        });
    }
    
    formatMonth(monthStr) {
        return new Date(monthStr + '-01').toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'short'
        });
    }
    
    closeModal() {
        document.getElementById('editModal').style.display = 'none';
    }
    
    showMessage(message, type) {
        // Remove existing messages
        const existingMessages = document.querySelectorAll('.message');
        existingMessages.forEach(msg => msg.remove());
        
        // Create new message
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${type}`;
        messageDiv.textContent = message;
        
        // Insert at top of main content
        const mainContent = document.querySelector('.main-content');
        mainContent.insertBefore(messageDiv, mainContent.firstChild);
        
        // Remove after 5 seconds
        setTimeout(() => {
            messageDiv.remove();
        }, 5000);
    }
}

// Global functions for HTML onclick handlers
window.clearFilters = function() {
    expenseTracker.clearFilters();
};

window.exportData = function() {
    expenseTracker.exportData();
};

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Create global instance
    window.expenseTracker = new ExpenseTracker();
});

// Note: Exports removed to avoid CORS issues when opening directly in browser
// For module use, uncomment the following line:
// export { ExpenseDatabase, ExpenseValidator, ExpenseTracker };
