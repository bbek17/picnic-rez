document.addEventListener('DOMContentLoaded', function() {
    var questions = document.querySelectorAll('.map-question');

    questions.forEach(function(question) {
        question.addEventListener('click', function() {
            var mapItem = this.parentNode;
            mapItem.classList.toggle('active');
        });
    });
});