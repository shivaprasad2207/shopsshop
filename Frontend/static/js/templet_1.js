
var drop_down_menu = '<nav class="navbar navbar-expand-sm bg-dark navbar-dark">' + 
                                                '<div class="collapse navbar-collapse" id="collapsibleNavbar">'+ 
                                                '<ul class="navbar-nav">'+
                                                ' <li class="nav-item">'+
                                                '{{#data}}  '+
                                                '<div class="btn-group">'+
                                                ' <button type="button" class="btn btn">{{category}}</button>'+
                                                '<button type="button" class="btn btn dropdown-toggle" data-toggle="dropdown">'+
                                                ' <span class="caret"></span>'+
                                                '</button>'+
                                                '<ul class="dropdown-menu" role="menu">'+
                                                ' {{#subcategories}}'+
                                                '<li><a href="#" onclick="javascript:get_item_types(\'{{sub_category_id}}\');return false;">{{sub_category}}</a></li>'+
                                                '{{/subcategories}}'  +
                                                '</ul>'+
                                                '</div>'+
                                                '{{/data}}'+
                                                ' </div>'  +
                                                '</nav>';
