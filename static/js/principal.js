// escuta pela tecla enter
document.addEventListener('keypress', (e) => {
    if(e.which == 13){
    	e.preventDefault();
    	document.getElementById("btn-login").click();
    }
});