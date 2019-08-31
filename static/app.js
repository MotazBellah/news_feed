const div = document.getElementById('news');
alert('h');
      // In case of click in UL, use the DOM traversal, to change the front-end side dynamically
      // By creating a form to submit the updating value to DB
      // Using Ajax request to update the page without refresh the page
div.addEventListener('click', (e) =>{
    alert('e');
    if (e.target.tagName.toLowerCase() === 'a'){
        const anchor = e.target;
    }
}
