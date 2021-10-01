
         // show districts registered on clicked province
    $(".provinc").change(function () {

    var $provinceid = $(this).children("option:selected").val();
    if ($provinceid==""){
     }else {

        $.ajax({
            type: "GET",
            url: "/filter/byprovince/" + $provinceid,
            async: false,
            dataType: 'json',
            success: function (data) {
                if (data != "") {
                  var html ;
                    data.forEach(function (dist_pro) {
                     html += '<option class="distdata" value="'+dist_pro.id+'">'+dist_pro.district+'</option>';
                     });
                    $("option[class='distdata']").remove(); //Before populate option value remeve previous data
                    $('.distric').append(html);
                    }else{
                        $("option[class='distdata']").remove(); // clear option items when selected  province does not have a district
                 }
                }
              ,
            error: function (data){
                    console.log(data);
                   } ,
        });
    }
    });


// show sectors registered on clicked district
    $(".distric").change(function () {

    var $districtid = $(this).children("option:selected").val();
    if ($districtid==""){
     }else {

        $.ajax({
            type: "GET",
            url: "/filter/bydistrict/" + $districtid,
            async: false,
            dataType: 'json',
            success: function (data) {
                if (data != "") {
                  var html ;
                    data.forEach(function (sect_distr) {
                     html += '<option class="sectdata" value="'+sect_distr.id+'">'+sect_distr.sector+'</option>';
                     });
                    $("option[class='sectdata']").remove(); //Before populate option value remeve previous data
                    $('.sect').append(html);
                    }else{
                        $("option[class='sectdata']").remove(); // clear option items when selected  province does not have a district
                 }
                }
              ,
            error: function (data){
                    console.log(data);
                   } ,
        });
    }
    });
