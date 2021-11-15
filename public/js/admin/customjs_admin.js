
/*         // show districts registered on clicked province
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
    });*/


             // #Modal image  when image is clicked
       $(".updatebtn").click(function() {

       var $mid  =    $(this).closest('tr').find('.id').text();
        $.ajax({
                type: "GET",
                url: "/find/member/"+$mid,
                async: false,
                dataType: 'json',
                success: function (data) {

              if (data !="") {
                 data.forEach(function (member_data) {

                    var fname =      member_data.fname
                    var lname =      member_data.lname
                    var tel_no =     member_data.tel_no
                    var email =      member_data.email
                    var address =    member_data.address

//                     member_data.tel_no
//                     member_data.tel_no



            $(".mod_mid").val($mid);
            $(".mod_fname").val(fname);
            $(".mod_lname").val(lname);
            $(".mod_tel").val(tel_no);
            $(".mod_email").val(email);
            $(".mod_address").val(address);

//             $(".mod_department").val(fname);
//            $(".mod_rolename").val(lname);

                         });
                       }
                   }
                });
        $('#updatemodal').modal('show'); // show update modal
    });



   $(".deletebtn").click(function() {

       var $mid  =    $(this).closest('tr').find('.id').text();

         $.ajaxSetup({
            headers: {
                'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
            }
        });

        $.ajax({
                type: "post",
                url: "/trash/member/"+$mid,
                async: false,
                dataType: 'json',
                data: {csrfmiddlewaretoken: window.CSRF_TOKEN},
                success: function (success) {
               window.location.href = "/view/member";
                },
               error:function (err) {
//               console.log(err)
//                   window.location.href = "/trash/member/"+$mid;
                                  window.location.href = "/view/member";

                }
             });

             });

   $(".printbtn").click(function() {

       var $mid  =      $(this).closest('tr').find('.id').text();
       var $fname  =    $(this).closest('tr').find('.fname').text();
       var $lname  =    $(this).closest('tr').find('.lname').text();
       var $tel  =      $(this).closest('tr').find('.tel').text();
       var $dept =      $(this).closest('tr').find('.dept').text();

       $("#namesid").text($fname + " " + $lname )
       $("#deptid").text($dept )
       $("#telid").text($tel )


       $('#qrcodeholder').qrcode({
		text	:$mid ,
		render	: "canvas",  // 'canvas' or 'table'. Default value is 'canvas'
		background : "#ffffff",
		foreground : "#000000",
		width : 115,
		height: 115
	    });

          $('#idcardmodal').modal('show'); // show print modal

             });


    $(".approvebtn").click(function() {    // when approve booking is clicked

       var $id  =    $(this).closest('tr').find('.id').text();

         $.ajaxSetup({
            headers: {
                'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
            }
        });

        $.ajax({
                type: "post",
                url: "/approve/booking/"+$id,
                async: false,
                dataType: 'json',
                data: {
                    id : $id,
                    csrfmiddlewaretoken: window.CSRF_TOKEN
                },
                success: function (success) {
                      console.log(success)

                },
               error:function (err) {
               console.log(err)
              window.location.href = "/approve/booking/"+$id;


                }
             });

             });


       $(".rejectbtn").click(function() {    // when approve booking is clicked

       var $id  =    $(this).closest('tr').find('.id').text();

         $.ajaxSetup({
            headers: {
                'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
            }
        });

        $.ajax({
                type: "post",
                url: "/reject/booking/"+$id,
                async: false,
                dataType: 'json',
                data: {
                    id : $id,
                    csrfmiddlewaretoken: window.CSRF_TOKEN
                },
                success: function (success) {
                      console.log(success)

                },
               error:function (err) {
               window.location.href = "/view/guest";

                }
             });

             });
