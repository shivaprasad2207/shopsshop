
function get_subcategory_list_on_iteminfo(){
               var val = document.getElementById('category_select').value ;
               document.getElementById('sub_category_list').value = '' ; 
               var vals = val.split('_');
               var category_id = vals[0];
               var shop_id = get_shop_id();
               var link = root_url + '/category/' + category_id + '/subcategory/';
               $.get(link,function(data){
                                $.get('/templet/admin_subcategory_list_to_item_info_1.html',function(info){  
                                      var link = root_url + '/shop/' + shop_id + '/category/' + category_id + '/';           
                                      $.get(link,function(data1){           
                                                d = {...data1,...data}
                                                var output = Mustache.render(info,d);
                                                document.getElementById('item_action').innerHTML = '';  
                                                document.getElementById('info_type_action').innerHTML = '';                                                 
                                                document.getElementById('sub_category_list').innerHTML = output;        
                                         });
                                     
                                  });
                               
                                },                                                                      
                                "json"
                );
               
}

function get_iteminfo_landing_page(){
                var val = document.getElementById('subcategory_select').value ;
                var infos = val.split('_');
                var subcategory = infos[2];
                var vals = val.split('/');
                var category_id = vals[2];
                var sub_category_id = vals[4];
                var shop_id = get_shop_id();
                var data1 = {
                              "subcategory":subcategory,
                              "category_id":category_id,
                              "sub_category_id":sub_category_id,
                              "shop_id": shop_id
                };
                var link = root_url + '/subcategory/' + sub_category_id + '/itemtype/';
                $.get(link,function(data){
                                                $.get('/templet/admin_itemtype_list_on_item_landing.html',function(info){                    
                                                                d = {...data1,...data};
                                                                var output = Mustache.render(info,d);
                                                                document.getElementById('info_type_action').innerHTML = output;               
                                                });
                                },
                                "json"
                );
}

function get_itemtype_list_landing_page(){
    var val = document.getElementById('itemtype_select').value ;
    var infos = val.split('_');
    var data = {
        'sub_category_id' : infos[0],
        'item_types_id': infos[1],
        'link': infos[2],
        'item_types': infos[3],
        'data':val
    };
    $.get('/templet/item_action_add_list.html',function(info){                    
                                                                var output = Mustache.render(info,data);
                                                                document.getElementById('item_action').innerHTML = output;               
                                                });
}

function get_item_list_form(d){
    var infos = d.split('_');
    var link = infos[2];
    $.get(root_url+link,function(data){
                                                $.get('/templet/admin_item_list_by_type.html',function(info){                    
                                                                var output = Mustache.render(info,data);
                                                                document.getElementById('disp1').innerHTML = output;
                                                                document.getElementById('disp2').innerHTML = ''; 
                                                });
                                },
                                "json"
                );
}

function get_item_add_form (d){
    var infos = d.split('_');
    var item_type = infos[3];
    var data = {
        'item_type': item_type,
        'data':d
    };
    $.get('/templet/admin_item_info_add_form.html',function(info){                    
                                                                var output = Mustache.render(info,data);
                                                                document.getElementById('disp2').innerHTML = '';    
                                                                document.getElementById('disp1').innerHTML = output;               
                                            });
}

function add_new_item (d){
    var str = $("#iteminfo_add_form").serialize();
    var s = str.replace(/%20/g, " ");
    var infos = s.split('&');
    var data = {};
    var sts = d.split('_');
    var link = sts[2];
    
    for (var i = 0 ; i < infos.length; i++){
        var tkv = infos[i];
        var kvs = tkv.split('=');
        data[kvs[0]] = kvs[1];
    }
    $.post(root_url+link,data, function(val, status,jqXHR){
                     get_item_list_form(d);
                },
                "json"
                );    
}

function get_item_info_form(link){
        $.get(root_url+link,function(data){
                                                $.get('/templet/admin_item_info_get.html',function(info){                    
                                                                var output = Mustache.render(info,data);
                                                                document.getElementById('disp2').innerHTML = output;               
                                                });
                                },
                                "json"
                );
}

function get_item_modify_form(link){
    $.get(root_url+link,function(data){
                                                $.get('/templet/admin_item_modify_form.html',function(info){                    
                                                                var output = Mustache.render(info,data);
                                                                document.getElementById('disp2').innerHTML = output;               
                                                });
                                },
                                "json"
                );
}

function modify_item(link){
    var str = $("#iteminfo_modify_form").serialize();
    var s = str.replace(/%20/g, " ");
    var infos = s.split('&');
    var data = {};
    
    for (var i = 0 ; i < infos.length; i++){
        var tkv = infos[i];
        var kvs = tkv.split('=');
        data[kvs[0]] = kvs[1];
    }
    var t_link_c = link.split('/'); 
    var redir = 'null_'+'null_'+ '/itemtype/' + t_link_c[2] + '/iteminfo/';
    $.ajax({
                                type: 'PUT',
                                url: root_url + link,
                                contentType: 'application/json',
                                data: JSON.stringify(data), // access in body
                }).done(function () {
                                console.log('SUCCESS');
                                get_item_list_form(redir); 
                }).fail(function (msg) {
                                console.log('FAIL');
                                get_item_list_form( redir );
                });
}


function del_item(link){
    var t_link_c = link.split('/');
    var redir = 'null_'+'null_'+ '/itemtype/' + t_link_c[2] + '/iteminfo/';
    $.ajax({
                                url: root_url + link,
                                type: 'DELETE',
                                success: function(result) {
                                                get_item_list_form(redir);
                                }
                });
}

function upload_item_image(link){
    $.get(root_url+link,function(data){
                                                $.get('/templet/upload.html',function(info){                    
                                                                var output = Mustache.render(info,data);
                                                                document.getElementById('disp3').innerHTML = output;               
                                                });
                                },
                                "json"
                );
    $.get('/templet/upload.html',function(info){
        
                                    document.getElementById('disp3').innerHTML = info;               
    });
}


function upload(file, item_types_id){
    var redir = 'null_'+'null_'+ '/itemtype/' + item_types_id + '/iteminfo/';
    var formData = new FormData();
    formData.append('file', $('#file')[0].files[0]);
    formData.append('rfile',file);
    $.ajax({
       url : '/cgi-bin/upload.py',
       type : 'POST',
       data : formData,
       processData: false,  // tell jQuery not to process the data
       contentType: false,  // tell jQuery not to set contentType
       success : function(data) {
           document.getElementById('disp3').innerHTML = '';
           get_item_list_form(redir);
       }
});
}