//Mustache Rendering System.
function render(target, template, data, mode){
	$.get(template, function(tmp) {
		var rendered = Mustache.render(tmp, data);

		//Append vs override mode
		if(mode == "APPEND_MODE"){
			$(target).append(rendered);
		}
		else{
			$(target).html(rendered);
		}
	});
}

//Render Textbooks List
function renderBookList(bl){
	$("#bookList").html("");
	$.each(bl, function(i, book){
		render("#bookList", "tp/book.html", {title: book.title, price: book.price, date_closing: book.date_closing, subject: book.subject, img: book.image, link: "bidBuyer.html?id="+book.id}, "APPEND_MODE")
	});
}

//Set Cookie Function
function setCookie(cname, cvalue, exdays){
	var d = new Date();
	d.setTime(d.getTime() + (exdays));
	var expires = "expires="+ d.toUTCString();
	document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}
////
//Fetch cookie by name
function getCookie(cname) {
	var name = cname + "=";
	var decodedCookie = decodeURIComponent(document.cookie);
	var ca = decodedCookie.split(';');
	for(var i = 0; i <ca.length; i++) {
		var c = ca[i];
		while (c.charAt(0) == ' ') {
			c = c.substring(1);
		}
		if (c.indexOf(name) == 0) {
			return c.substring(name.length, c.length);
		}
	}
	return "";
}


function menu(){

	//Get Token
	token = getCookie("session");

	//If unset
	if (token == null){
	    render("#menu", "tp/menu.html", {auth_action: "login.html", auth_link: "Login"})
	}

	$.ajax({
		type: 'POST',
		url: 'http://127.0.0.1:5000/login/check',
		data: '{"token": "'+token+'"}',
		contentType:"application/json",
		dataType: 'json',
		success: function(res){
		    if(res.status == 'success'){
			    render("#menu", "tp/menu.html", {auth_action: "logout.html", auth_link: "Logout"})
		    }
		    else{
		        render("#menu", "tp/menu.html", {auth_action: "login.html", auth_link: "Login"})
		    }
		},
		failure: function(res){
			render("#menu", "tp/menu.html", {auth_action: "login.html", auth_link: "Login"})
		}
	});

}

//System Alerts
function alert(val){
	$.get("components/alert.html", function(alrt) {
		$("body").prepend(alrt);
		$("#alert_modal_content").text(val);
		$('html,body').animate({scrollTop:0},0);
		$("#alert_modal").fadeIn({ duration: 500, queue: false }).css('display', 'none').slideDown(500).delay(3500).animate({ height: 'toggle', opacity: 'toggle' }, 'slow', function() { $(this).remove(); });


		//$("").fadeIn("fast").delay(3500).fadeOut(700, );
	});
}

function getQueryVariable(variable){
    var query = window.location.search.substring(1);
    var vars = query.split("&")
    for (var i = 0; i<vars.length; i++){
        var pair = vars[i].split("=");
        if (pair[0]==variable){return pair[1];}
    }
    return(false);
}

 //Check any queued messages
 function persistentAlert(){
   message = getCookie("msg");
   console.log(message)
    if(message.length > 2){
     alert(message);
    }
   setCookie("msg", "", -1000000);
  }
