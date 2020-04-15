var root_url = 'http://127.0.0.1:8000'

function show_category(){
        var shop_id = get_shop_id();
        var url = root_url + '/shop-menu/' + shop_id  +  '/';
        $.get('/templet/drop_down.html',function(info){
                $.ajax({
                        url: url,
                        type: 'GET',
                        crossDomain: true,
                        success: function(data) {
                                output = Mustache.render(info,data);
                                document.getElementById('div3').innerHTML = output;
                        },
                        error: function() { alert('Failed!'); }
                });      
        })
}

function get_item_types(id){
        $.get('/templet/item_type_display.html',function(info){
                $.ajax({
                        url: root_url + '/subcategory/' + id + '/itemtype/' ,
                        type: 'GET',
                        crossDomain: true,
                        success: function(data) {
                                output = Mustache.render(info,data);
                                document.getElementById('div4').innerHTML = output;
                        },
                        error: function() { alert('Failed!'); }
                });      
        })
}


function get_grid_view(info,col){
        var table_open = '<table class="table table-bordered">';
        var table_close = '</table>';
        var table_row_open = '<tr>';
        var table_row_close = '</tr>';
        var table_col_open = '<td>';
        var table_col_close = '</td>';
        var exp = table_open + table_row_open ;
        
        for (var i = 0 ; i <  info.length ; i++ ){
                m = i % col;
                if ( i == 0 || m){
                        exp = exp + table_col_open + 
                        
                        '<a href="#" onclick="javascript:get_item_info(\''+  info[i]['item_info_id']   +'\');return false;">' + 
                        '<img class="card-img-top" style="width:180px;height:200px;" src="/static/images/shopsshps/' + info[i]['item_image']+ '.jpg\"' + 'alt="Card image cap">' + 
                        '<br>' + info[i]['item_name'] + '<br>Price:' +  info[i]['item_unit_price'] + '<br> Per -'+ info[i]['item_minimum_qty'] +
                        '/' + info[i]['item_unit'] +'<br>' + '</a>'
                        
                        + table_col_close;
                }else{
                        exp = exp + table_row_close + table_row_open;
                        exp = exp + table_col_open +
                        
                        '<a href="#" onclick="javascript:get_item_info(\''+  info[i]['item_info_id']   +'\');return false;">' + 
                        '<img class="card-img-top" style="width:180px;height:200px;" src="/static/images/shopsshps/' + info[i]['item_image']+ '.jpg\"' + 'alt="Card image cap">' + 
                        '<br>' + info[i]['item_name'] + '<br>Price:' +  info[i]['item_unit_price'] + '<br> Per -'+ info[i]['item_minimum_qty'] +
                        '/' + info[i]['item_unit'] +'<br>' + '</a>'
                        
                        + table_col_close;
                }
        }
        length = info.length ;
        while  (length % col){
              exp = exp + table_col_open + 'No Info' + table_col_close;
              length++;  
        }
        exp = exp + table_row_close + table_close;     
        return exp;
}

function get_item_infos(id){
        var link = root_url + '/itemtype/' + id + '/iteminfo/';
        var col = 3 ;
        $.get(link,function(data){
                                        var info = get_grid_view(data['data'],col);
                                        document.getElementById('disp').innerHTML =  info;               
                                                
                                },
                                "json"
                );
}


function get_item_info(id){
        alert ('item_info ' + id);
}


