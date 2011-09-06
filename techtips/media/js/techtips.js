/**
 * The techtips object is the namespace into which we put all techtips-related 
 * functionality.
 */
var techtips = function () {
    
    // Public
    return {
        /**
         * load_tip loads a techtip asynchronously, and then hides it if the 
         * user click on the title a second time. 
         */
        load_tip: function () {
            var original_href = $(this).attr('href'); 
            $(this).attr('href', '#');
            $(this).click(function () {
                // Load list item content asynchronously
                $(this).parent().parent().find('div.list_item_outer').load(
                    original_href + 'ajax/'
                );
                // Now redefine click handler to simple toggle
                $(this).unbind('click');
                $(this).click(function () {
                    $(this).parent().parent().find('div.list_item_outer').toggle();
                    return false;
                });
                
                return false;
            });
        }
        
    };
}();


$(document).ready(function () {
    // Change anchors to AJAX
    $('div.list_item > h2 > a').each(techtips.load_tip);
    
    // Remove pagination
    //$('nav.pagination').remove();
    
    // Add async content loader at bottom of page
    // TODO: ...
});
