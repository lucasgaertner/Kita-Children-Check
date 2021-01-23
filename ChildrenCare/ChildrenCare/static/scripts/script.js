const location_arr = ['data', 'about', 'signup', 'login'];

function setHeader(){
    var currenturl = window.location.href;
    var header_split = currenturl.split('/');
    var last = header_split[header_split.length-2];
    var login = header_split[header_split.length-4];
    for (i=0; i < location_arr.length; i++){
        if (location_arr[i] == last){
            var tmp_site = document.getElementById(location_arr[i]);
            tmp_site.classList.add('active');
        }
        else if (last == "127.0.0.1:8000" || last == "localhost:8000"){
            var tmp_site = document.getElementById('home');
            tmp_site.classList.add('active');
        }
        else if(login == "login"){
            var tmp_site = document.getElementById('login');
            tmp_site.classList.add('active');
            var tmp_last = header_split[header_split.length-2];
            changedHeader(tmp_last);
        }
        else if(last == "?next="){
            var tmp_site = document.getElementById('login');
            tmp_site.classList.add('active');
        }
    }
}

function changedHeader(link){
    var old_site = document.getElementById(link);
    old_site.classList.remove('active');
}

