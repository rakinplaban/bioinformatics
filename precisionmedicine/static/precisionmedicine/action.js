document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('#addpatients').addEventListener('click', ()=> {
        document.querySelector('.bg-model').style.display = 'flex';
    });

    document.querySelector('.close').addEventListener('click', ()=> {
        document.querySelector('.bg-model').style.display = 'none';
    });
    
    document.querySelector('#adddisease').addEventListener('click', ()=> {
        document.querySelector('.bg-model-5').style.display = 'flex';
    });

    document.querySelector('.close-5').addEventListener('click', ()=> {
        document.querySelector('.bg-model-5').style.display = 'none';
    });
    

})