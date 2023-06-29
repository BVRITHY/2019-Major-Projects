jQuery(document).ready(function() {
    jQuery('.slider-carousel').jcarousel({
    	scroll: 1,
        wrap: 'both',
        start:1,
        auto:4,
        visible:1,
        initCallback: mycarousel_initCallback
    });
});

function mycarousel_initCallback(carousel)
{
	Cufon.refresh();
    // Disable autoscrolling if the user clicks the prev or next button.
    carousel.buttonNext.bind('click', function() {
        carousel.next();
    });
 
    carousel.buttonPrev.bind('click', function() {
        carousel.prev();
    });
 
};


$(function(){
    $('.blink').
        focus(function() {
            if(this.title==this.value) {
                this.value = '';
            }
        }).
        blur(function(){
            if(this.value=='') {
                this.value = this.title;
            }
        });
})

function pageLoaded() {
	Cufon.replace('.info h2', { fontFamily: 'Chaparral Pro'});
	
}