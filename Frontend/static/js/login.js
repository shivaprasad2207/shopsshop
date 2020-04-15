var root_url = 'http://127.0.0.1:8000';
var main_page = 'http://localhost/cgi-bin/admin_login.py';

function get_user_login_form( ){
    var link = root_url+'/shops/';
    $.get(link,function(data){
                        $.get('/templet/admin_user_login_form.html',function(info){                     
                                        var output = Mustache.render(info,data);
                                        document.getElementById('usr_login').innerHTML = output;               
                                    });
                                },
                                "json"
                );               
}


function user_login(){
            var str = $("#user_login_form").serialize();
            var s1 = str.replace(/%20/g, " ");
            var s = s1.replace(/%40/g, "@");
            var infos = s.split('&');
            var data = {};
            for (var i = 0 ; i < infos.length; i++){
                var tkv = infos[i];
                var kvs = tkv.split('=');
                data[kvs[0]] = kvs[1];
            }
            var link = root_url+'/usr-auth?shop_token='+data['shop_token']+'&usr_email='+data['usr_email']+'&usr_password='+data['usr_password']
            $.ajax({
                        url: link,
                        type: 'GET',
                        crossDomain: true,
                        success: function(data, status, xhr) {
                                        document.cookie = "__C__shop_id="+String(data['shop_id']) + " ;" ;
                                        document.cookie = "__C__shop_token="+data['shop_token'] + " ;" ;
                                        get_user_page_divs();
                                },
                        error: function(xhr, timeout, message) {
                                alert('failed');
                        }
                });
}


function get_user_page_divs(){
    $.get('/templet/user_page_divs.html',function(info){                    
                        document.getElementById('login_page').innerHTML = info;
                        var shop_id = get_shop_id();       
                        var url = root_url+'/shop/'+shop_id+'/' ;
                        $.get(url,function(data){        
                                $.get('/templet/navBar.html',function(info){
                                                var output = Mustache.render(info,data);
                                                $("#div1").html(output);
                                });
                        },
                         "json"
                        );
    });   
}

function get_admin_login_form(link){
    $.get('/templet/admin_store_login.html',function(info){                    
                        document.getElementById('admin_login').innerHTML = info;               
    });                            
}

function get_store_register_form (){
    $.get('/templet/admin_store_register.html',function(info){                    
                document.getElementById('store_create').innerHTML = info;               
    });
}

function store_register(){
    var str = $("#store_reg_form").serialize();
    var s1 = str.replace(/%20/g, " ");
    var s = s1.replace(/%40/g, "@");
    var infos = s.split('&');
    var data = {};
    var link = '/new-shop/';
    for (var i = 0 ; i < infos.length; i++){
        var tkv = infos[i];
        var kvs = tkv.split('=');
        data[kvs[0]] = kvs[1];
    }
    $.post(root_url+link, data, function(val, status,jqXHR){
                     window.location.href = main_page
                },
                "json"
                );
    
}


function get_user_register_form(){
     var link = root_url+'/shops/';
     $.get(link,function(data){
                                                $.get('/templet/admin_user_register_form.html',function(info){                    
                                                                var output = Mustache.render(info,data);
                                                                document.getElementById('usr_create').innerHTML = output;               
                                                });
                                },
                                "json"
                );
}

function user_register(){
    var str = $("#user_reg_form").serialize();
    var s1 = str.replace(/%20/g, " ");
    var s = s1.replace(/%40/g, "@");
    var infos = s.split('&');
    var data = {};
    var link = '/usr-login/';
    for (var i = 0 ; i < infos.length; i++){
        var tkv = infos[i];
        var kvs = tkv.split('=');
        data[kvs[0]] = kvs[1];
    }
     $.post(root_url+link,data, function(val, status,jqXHR){
                    window.location.href = main_page 
                },
                "json"
                );    
    //alert (JSON.stringify(data));
}