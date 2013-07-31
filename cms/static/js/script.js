/* Author: 
David Alan Vogler, 2011


*/


 $(document).ready(function(){
 
 $('.work-image-list').each(function() {
 	//multiple cycle slideshows on one page
     var $this = $(this), $ss = $this.closest('.work-image-slideshow');
     var prev = $ss.find('a.prev'), next = $ss.find('a.next');
     $this.cycle({
         fx:     'fade', 
         speed:  'fast', 
         timeout: 0, 
         next:   next, 
         prev:   prev 
     });
 });
 
 //fancybox for portfolio images
 
 $(".fancybox").fancybox({
		openEffect	: 'none',
		closeEffect	: 'none'
	});
 
 //cookie-controlled status of collapsible about box
 
 var toggler_status = $.cookie("about_dav");
 
 if(toggler_status == null){// cookie not set
	 $('.closed').hide();
	 $('.open').show();;
 };
 
 if(toggler_status == "open"){ // if cookie set to open state
	 $('.closed').hide();
	 $('.open').show();
 };
 
 if(toggler_status == "closed"){
 	$('#about').slideUp('fast');
 	$('.watbar').toggleClass("dotbot");
 	$('.open').hide();
 	$('.closed').show();
 	$.cookie("about_dav", "closed", {expires: 7}); 
 };

 
 $('.open').click(function(){ //box is open, this hides the about box
 	$('#about').slideUp('slow');
 	$('.watbar').toggleClass("dotbot");
 	$('.open').hide();
 	$('.closed').show();
 	$.cookie("about_dav", "closed", {path: '/', expires: 7});//set cookie to closed
 
 });
 
 
 $('.closed').click(function(){// box is hidden, this opens it
 	$('#about').slideDown('slow');
 	$('.watbar').toggleClass("dotbot");
 	$('.closed').hide();
 	$('.open').show();
 	$.cookie("about_dav", "open", {path: '/', expires: 7});//set cookie to open
 		
 
 });
 
 // http://css-tricks.com/NetMag/FluidWidthVideo/Article-FluidWidthVideo.php
 
 // Find all YouTube and Vimeo videos
 var $allVideos = $("iframe[src^='http://player.vimeo.com'], iframe[src^='http://www.youtube.com']"),
 
     // The element that is fluid width
     $fluidEl = $("figure");
 
 // Figure out and save aspect ratio for each video
 $allVideos.each(function() {
 
   $(this)
     .data('aspectRatio', this.height / this.width)
 
     // and remove the hard coded width/height
     .removeAttr('height')
     .removeAttr('width');
 
 });
 
 // When the window is resized
 $(window).resize(function() {
 
   var newWidth = $fluidEl.width();
 
   // Resize all videos according to their own aspect ratio
   $allVideos.each(function() {
 
     var $el = $(this);
     $el
       .width(newWidth)
       .height(newWidth * $el.data('aspectRatio'));
 
   });
 
 // Kick off one resize to fix all videos on page load
 }).resize();
 


});

