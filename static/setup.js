let currentStep = 0; // 当前步骤
const totalSteps = 3; // 总步骤数
let quetion_list = ["tell me the name of your produt", "give me a brief introduction of the product",
                    "What does your product's user profile look like"]
document.addEventListener('DOMContentLoaded', function () {
    updateStep();
});

function updateStep() {
    const inputSection = document.getElementById('inputSection');
    inputSection.innerHTML = ''; 
    const input = document.createElement('input');
    input.type = 'text';
    input.id = 'input' + currentStep;
    input.placeholder = quetion_list[currentStep];
    inputSection.appendChild(input);
}

function submitForm() {
    const input = document.getElementById('input' + currentStep);
    const value = input.value;
    console.log('Step ' + (currentStep + 1) + ' input:', value);

    fetch('/submit', {
        method: 'POST',
        body: value,
    })

    if (currentStep < totalSteps - 1) {
        currentStep++;
        updateStep(); 
    } else {
        console.log('All steps completed');
        window.location.href = '/result'; 
    }
}
