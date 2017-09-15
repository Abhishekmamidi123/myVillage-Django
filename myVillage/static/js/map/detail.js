$('[data-toggle=tab]').click(function(){
  if ($(this).parent().hasClass('active')){
	$($(this).attr("href")).toggleClass('active');
  }
})
