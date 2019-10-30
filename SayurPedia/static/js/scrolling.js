$(window).scroll(function(){
	var scroll = $(window).scrollTop();
	
	if(scroll >= 300){
		$("#nav1").addClass("bg-dark");
	}else{
		$("#nav1").removeClass("bg-dark");
	}
});

