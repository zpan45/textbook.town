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
		render("#bookList", "tp/book.html", {title: book.title, price: book.price, date_closing: book.date_closing, subject: book.subject, img: book.image}, "APPEND_MODE")
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