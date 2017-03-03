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