function toggleAnswer(id) {
    const answerDiv = document.getElementById(id);
    if (answerDiv.classList.contains('hidden')) {
        answerDiv.classList.remove('hidden');
    } else {
        answerDiv.classList.add('hidden');
    }
}
