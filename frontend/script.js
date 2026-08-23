document.getElementById('predict_button').onclick = function() {
    const inputText = document.getElementById('review_input').value;
    predict(inputText);
}


async function predict(inputText) {

    const response = await fetch('http://localhost:8000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            review: inputText
        })
    });

    const data = await response.json();

    displayPrediction('model1', data.model1);
    displayPrediction('model2', data.model2);
    displayPrediction('model3', data.model3);
}


function displayPrediction(modelClass, prediction) {

    const element = document.getElementsByClassName(modelClass)[0];

    // Remove previous color
    element.classList.remove(
        'positive_prediction',
        'negative_prediction',
        'neutral_prediction'
    );

    if (prediction === 1) {

        element.innerHTML = "POSITIVE";
        element.classList.add('positive_prediction');

    } else if (prediction === -1) {

        element.innerHTML = "NEGATIVE";
        element.classList.add('negative_prediction');

    } else {

        element.innerHTML = "NEUTRAL";
        element.classList.add('neutral_prediction');
    }
}