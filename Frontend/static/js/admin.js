var root_url = 'http://127.0.0.1:8000';
var admin_page = 'http://localhost/cgi-bin/admin.py'; 

$(document).ready(function(){
                $.get('/templet/admin_navBar.html',function(info){
                        $("#diva1").html(info);
                });
});


function get_cookies(){
  var pairs = document.cookie.split(";");
  var cookies = {};
  for (var i=0; i<pairs.length; i++){
    var pair = pairs[i].split("=");
    cookies[(pair[0]+'').trim()] = unescape(pair.slice(1).join('='));
  }
  return cookies;
}

function get_shop_id(){
                var shop_id_ck_name = '__C__shop_id';
                c = get_cookies();
                return c[shop_id_ck_name];
}

function admin_signin(){
                var email = $("#inputEmail").val() ; 
                var password = $("#inputPassword").val(); 
                $.ajax({
                        url: root_url + '/shop-login?shop_email=' + email + '&shop_password=' + password,
                        type: 'GET',
                        crossDomain: true,
                        success: function(data, status, xhr) {
                                        document.cookie = "__C__shop_id="+String(data['shop_id']) + " ;" ;
                                        document.cookie = "__C__shop_token="+data['shop_token'] + " ;" ;
                                        window.location.href = admin_page;
                                },
                        error: function(xhr, timeout, message) {
                                alert('failed');
                        }
                });
}

function get_settings_menu(){
        var menu = {
                       "attrs":[{ "attr":"category"}, { "attr":"subcategory"}, { "attr":"item type"}, { "attr":"item info"} ]
                   };
        $.get('/templet/admin_drop_down.html',function(info){
                output = Mustache.render(info,menu);
                document.getElementById('diva3').innerHTML = output;
        })
}

function get_add_category_form (){
                $.get('/templet/admin_category_add_form.html',function(info){
                        document.getElementById('disp').innerHTML = info;
                })
}

function add_category(){
                var id = get_shop_id();                
                var url = root_url + '/shop/' + id + '/category/';
                var paramJson = {
                        'category':document.getElementById('category').value
                   }
            
                $.post(url,paramJson, function(data, status,jqXHR){
                     get_category_list_page();
                },
                "json"
                );
}

function get_category_list_page(){
                var id = get_shop_id();
                var url = root_url + '/shop/'+ id +'/category/';
                $.get(url,function(data){
                      $.get('/templet/admin_category_list.html',function(info){
                                output = Mustache.render(info,data);
                                document.getElementById('disp').innerHTML = output;
                      
                      })
                     },
                     "json"
                );
}

function del_category(id,link){
                $.ajax({
                                url: root_url + link,
                                type: 'DELETE',
                                success: function(result) {
                                                get_category_list_page();
                                }
                });
}

function get_category_modify_form(id,link){
         var url = root_url + link ;
         $.get(url,function(data){
                $.get('/templet/get_category_modify_form.html',function(info){
                                output = Mustache.render(info,data);
                                document.getElementById('disp').innerHTML = output;
                      
                      })             
           },
           "json"
        );
}

function admin_modify_category(link){
                var paramJson = {
                        'category':document.getElementById('category').value,
                        'shop_id': get_shop_id()
                }
                $.ajax({
                                type: 'PUT',
                                url: root_url + link,
                                contentType: 'application/json',
                                data: JSON.stringify(paramJson), // access in body
                }).done(function () {
                                console.log('SUCCESS');
                                get_category_list_page();
                }).fail(function (msg) {
                                console.log('FAIL');
                                get_category_list_page();
                });
}

function get_subcategory_list_page(category_id, link){
                var url = root_url + '/category/' + category_id + '/subcategory/';
                $.get(url,function(data){          
                                                $.get('/templet/admin_subcategory_list.html',function(info){
                                                        data['category_id'] = category_id;       
                                                        var output = Mustache.render(info,data);
                                                        document.getElementById('disp1').innerHTML = output;
                                                        document.getElementById('disp2').innerHTML = '';
                                                        
                                                });
                                },                                                                      
                                "json"
                );
                
}

function get_subcategory_add_form (category_id){
                var id = get_shop_id();
                var link = root_url + '/shop/'+ id +'/category/'+ category_id;                               
                $.get(link,function(data){
                                url = '/category/' + category_id + '/subcategory/';
                                $.get('/templet/admin_subcategory_add_form.html',function(info){
                                                var data_block = {'url':url, 'category':data['category'] , 'category_id':data['category_id'] };    
                                                var output = Mustache.render(info,data_block);
                                                document.getElementById('disp2').innerHTML = output;        
                                     });
                                },                                                                      
                                "json"
                );
}

function get_subcategory_modify_form(category_id, sub_category_id,link){
                $.get(root_url+link,function(data){ 
                                $.get('/templet/admin_subcategory_modify_form.html',function(info){
                                                var output = Mustache.render(info,data);
                                                document.getElementById('disp2').innerHTML = output;
                                  });
                                },                                                                      
                                "json"
                );
}

function modify_subcategory(link,sub_category_id,category_id){
                var paramJson = {
                        'sub_category':document.getElementById('subcategory').value,
                        'category_id': category_id
                }
                $.ajax({
                                type: 'PUT',
                                url: root_url + link,
                                contentType: 'application/json',
                                data: JSON.stringify(paramJson), // access in body
                }).done(function () {
                                console.log('SUCCESS');
                                get_subcategory_list_page(category_id, link);
                }).fail(function (msg) {
                                console.log('FAIL');
                                get_subcategory_list_page(category_id, link);
                });
}

function add_subcategory (url,category_id){       
                var paramJson = {
                        "sub_category": document.getElementById('subcategory').value
                }
            
                $.post(root_url+url, paramJson, function(data, status,jqXHR){
                     get_subcategory_list_page(category_id,'none');
                },
                "json"
                );
}

function del_subcategory (category_id, sub_category_id, link){
                $.ajax({
                                url: root_url + link,
                                type: 'DELETE',
                                success: function(result) {
                                                get_subcategory_list_page(category_id,'none');
                                }
                });
}


function get_subcategory_list_on_itemtype(){
               var val = document.getElementById('category_select').value ;
               document.getElementById('sub_category_list').value = '' ; 
               var vals = val.split('_');
               var category_id = vals[0];
               var shop_id = get_shop_id();
               var link = root_url + '/category/' + category_id + '/subcategory/';
               $.get(link,function(data){
                                $.get('/templet/admin_subcategory_list_to_item_info.html',function(info){  
                                      var link = root_url + '/shop/' + shop_id + '/category/' + category_id + '/';           
                                      $.get(link,function(data1){           
                                                d = {...data1,...data}
                                                var output = Mustache.render(info,d);
                                                document.getElementById('info_type_action').innerHTML = '';
                                                document.getElementById('sub_category_list').innerHTML = output;        
                                         });
                                     
                                  });
                               
                                },                                                                      
                                "json"
                );
               
}

function get_itemtype_landing_page(){
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
                                                $.get('/templet/admin_itemtype_list_page.html',function(info){                    
                                                                d = {...data1,...data};
                                                                var output = Mustache.render(info,d);
                                                                document.getElementById('disp1').innerHTML = output;
                                                                document.getElementById('disp2').innerHTML = '';                
                                                });
                                },
                                "json"
                );
}

function get_itemtype_add_form(info){
                var infos = info.split('_');
                var data = {
                                "sub_category_id" : infos[0],
                                "subcategory":infos[1]
                }
                $.get('/templet/admin_item_type_add_form.html',function(info){                    
                                                                var output = Mustache.render(info,data);
                                                                document.getElementById('disp2').innerHTML = output;                
                                                });
}


function add_item_type(sub_category_id){
                var url = root_url + '/subcategory/' + sub_category_id + '/itemtype/'
                var item_types = document.getElementById('item_type').value ;
                var paramJson = {
                          'item_types': item_types,
                          'sub_category_id':sub_category_id
                }
                $.post(url,paramJson, function(data, status,jqXHR){
                     get_itemtype_landing_page();
                },
                "json"
                );
}


function get_itemtype_modify_form (d){
                var infos = d.split('_'); 
                var sub_category_id = infos[0];
                var item_types_id = infos[1];
                var url = root_url + '/subcategory/' + sub_category_id + '/itemtype/' + item_types_id + '/';
                $.get(url,function(data){
                                                $.get('/templet/admin_item_type_modify_form.html',function(info){                    
                                                                var output = Mustache.render(info,data);
                                                                document.getElementById('disp2').innerHTML = output;
                                                });
                                },
                                "json"
                );
}

function modify_item_type(link){
                var data  = {'item_types' : document.getElementById('item_type').value } ;
                $.ajax({
                                type: 'PUT',
                                url: root_url + link,
                                contentType: 'application/json',
                                data: JSON.stringify(data), // access in body
                }).done(function () {
                                console.log('SUCCESS');
                                get_itemtype_landing_page();
                }).fail(function (msg) {
                                console.log('FAIL');
                                get_itemtype_landing_page();
                });
}




function del_itemtype(d){
                var infos = d.split('_');
                var sub_category_id = infos[0];
                var item_types_id = infos[1];
                var link = '/subcategory/' + sub_category_id + '/itemtype/' + item_types_id + '/' ;
                $.ajax({
                                url: root_url + link,
                                type: 'DELETE',
                                success: function(result) {
                                                get_itemtype_landing_page();
                                }
                });   
}