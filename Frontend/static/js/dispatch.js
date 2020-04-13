
function get_landing_page(type,id){
          if (type == 'category'){
                $.get('/templet/admin_category_setting_landing.html',function(info){
                        document.getElementById('diva4').innerHTML = info;
                })
          };
          if (type == 'subcategory'){
                var id = get_shop_id();
                var url = root_url + '/shop/'+ id +'/category/';
                $.get(url,function(data){          
                                                $.get('/templet/admin_subcategory_setting_landing.html',function(info){
                                                        var output = Mustache.render(info,data);
                                                        document.getElementById('diva4').innerHTML = output;        
                                                });
                                },                                                                      
                                "json"
                );
          }
          if (type == 'item type'){
                var id = get_shop_id();
                var url = root_url + '/shop/'+ id +'/category/';
                $.get(url,function(data){          
                                                $.get('/templet/admin_item_type_landning_page.html',function(info){
                                                        var output = Mustache.render(info,data);
                                                        document.getElementById('diva4').innerHTML = output;        
                                                });
                                },                                                                      
                                "json"
                );
          }
          if (type == 'item info' ){
                var id = get_shop_id();
                var url = root_url + '/shop/'+ id +'/category/';
                $.get(url,function(data){          
                                                $.get('/templet/admin_item_landning_page.html',function(info){
                                                        var output = Mustache.render(info,data);
                                                        document.getElementById('diva4').innerHTML = output;        
                                                });
                                },                                                                      
                                "json"
                );
          }    
}
