// Get DOM elements
const ingredientsInput = document.getElementById('ingredients');
const analyzeBtn = document.getElementById('analyzeBtn');
const resultsSection = document.getElementById('results');
const loadingSection = document.getElementById('loading');
const errorSection = document.getElementById('error');
const errorMessage = document.getElementById('errorMessage');

// Results elements
const ratingValue = document.getElementById('ratingValue');
const ratingProgress = document.getElementById('ratingProgress');
const healthLevel = document.getElementById('healthLevel');
const healthDescription = document.getElementById('healthDescription');
const analyzedIngredients = document.getElementById('analyzedIngredients');

// Example buttons
const exampleButtons = document.querySelectorAll('.btn-example');

// Health descriptions
const healthDescriptions = {
    'Excellent': 'These ingredients are highly nutritious and beneficial for your health. Great choice!',
    'Good': 'These ingredients are generally healthy with some nutritional value.',
    'Moderate': 'These ingredients are acceptable but could be improved with healthier alternatives.',
    'Poor': 'These ingredients may have limited nutritional value or contain unhealthy components.',
    'Very Poor': 'These ingredients are likely unhealthy and should be consumed sparingly or avoided.'
};

// Add event listener to analyze button
analyzeBtn.addEventListener('click', analyzeIngredients);

// Add event listeners to example buttons
exampleButtons.forEach(button => {
    button.addEventListener('click', () => {
        ingredientsInput.value = button.dataset.example;
        analyzeIngredients();
    });
});

// Allow Enter key to submit (Ctrl+Enter for new line in textarea)
ingredientsInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        analyzeIngredients();
    }
});

async function analyzeIngredients() {
    const ingredients = ingredientsInput.value.trim();
    
    // Validate input
    if (!ingredients) {
        showError('Please enter some ingredients to analyze.');
        return;
    }
    
    // Show loading state
    hideAllSections();
    loadingSection.classList.remove('hidden');
    analyzeBtn.disabled = true;
    
    try {
        // Make API request
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ ingredients: ingredients })
        });
        
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'Failed to analyze ingredients');
        }
        
        const data = await response.json();
        
        // Display results
        displayResults(data, ingredients);
        
    } catch (error) {
        console.error('Error:', error);
        showError(error.message || 'Failed to connect to the server. Please try again.');
    } finally {
        analyzeBtn.disabled = false;
    }
}

function displayResults(data, ingredients) {
    hideAllSections();
    
    // Update rating value
    ratingValue.textContent = data.rating;
    
    // Update health level
    healthLevel.textContent = data.level;
    healthLevel.style.color = data.color;
    
    // Update health description
    healthDescription.textContent = healthDescriptions[data.level] || '';
    
    // Update analyzed ingredients
    analyzedIngredients.textContent = ingredients;
    
    // Animate rating circle
    const circumference = 534;
    const progress = (data.rating / 10) * circumference;
    const dashOffset = circumference - progress;
    
    ratingProgress.style.stroke = data.color;
    ratingProgress.style.strokeDashoffset = dashOffset;
    
    // Show results with animation
    resultsSection.classList.remove('hidden');
    resultsSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

function showError(message) {
    hideAllSections();
    errorMessage.textContent = message;
    errorSection.classList.remove('hidden');
}

function hideAllSections() {
    resultsSection.classList.add('hidden');
    loadingSection.classList.add('hidden');
    errorSection.classList.add('hidden');
}

// Add some interactivity to the textarea
ingredientsInput.addEventListener('input', () => {
    if (ingredientsInput.value.trim()) {
        analyzeBtn.style.opacity = '1';
    } else {
        analyzeBtn.style.opacity = '0.8';
    }
});
