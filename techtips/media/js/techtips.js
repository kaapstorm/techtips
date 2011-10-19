/**
 * This file is part of Tech Tip of the Day.
 *
 * Tech Tip of the Day is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * Tech Tip of the Day is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with Tech Tip of the Day.  If not, see <http://www.gnu.org/licenses/>.
 */ 

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
        },
        
        /**
         * to_button converts [<a href="#">Text</a>] to a button
         */
        to_button: function () {
            // Get href
            var href = $(this).children('a').attr('href');
            // Get text
            var text = $(this).children('a').html();
            var button = '\
<button onclick="document.location.href=\'' + href + '\'; \
                 return false;">' + text + '</button>';
            $(this).replaceWith(button);
        }
        
    };
}();
