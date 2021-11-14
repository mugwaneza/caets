(function ($) {
 "use strict";
 // Validation for order form
		$(".add-professors").validate(
		{					
			rules:
			{	
				firstname:
				{
					required: true
				},
				lastname:
				{
					required: true
				},
				email:
				{
					required: true,
					email: true
				},
				username:
				{
					required: true,
					minlength:5
				},
				password:
				{
					required: true,
					minlength:8
				},

				photo:
				{
					required: true
				},
				address:
				{
					required: true
				},
				tel:
				{required: true,
                 minlength:10,
                 maxlength:10
				},
				nid:
				{required: true
				},

				district:
					{
				required: true
				},

				sectorname:
					{
				required: true
				},
				phonenumber:
					{
				required: true,
				 minlength:10,
                 maxlength:10
				},
				department:
					{
				required: true
				},
				fullname:
					{
				required: true
				},
				village:
					{
				required: true
				},
				sector:
					{
				required: true
				},
				visit_reason:
					{
				required: true
				},
                 rolename:
				{
                  required: true
				},
                 student:
				{
                  required: true
				},
                 amount:
				{
                  required: true
				},
                 balance:
				{
                  required: true
				},
                 role:
				{
                  required: true
				}
			},
			messages:
			{	
				firstname:
				{
					required: 'Please enter first name'
				},
				lastname:
				{
					required: 'Please enter last name'
				}
				,
				username:
				{
					required: 'Please enter username'
				},
				password:
				{
					required: 'Please enter password'
				},
				email:
				{
					required: 'Please enter your email address'
				},
				photo:
				{
					required: 'Photo is required'
				},
				address:
				{
					required: 'Please enter address'
				},
				tel:
				{
					required: 'Telephone is required'
				}
                ,districtname:
				{
					required: 'District can be empty'
				},
				phonenumber:
				{
					required: 'please enter telephone'
				},
            department:
				{
					required: 'Select department'
				},
            fullname:
				{
					required: 'Full name is required'
				}
                  ,
            village:
				{
					required: 'Village is  required'
				} ,
            sector:
				{
					required: 'sector is  required'
				},
            district:
				{
					required: 'district is  required'
				},
             nid:
				{
					required: 'Nation Id is  required'
				},
             visit_reason:
				{
					required: 'Visit reason is  required'
				},
				rolename:
				{
					required: 'Role is required'
				},
                student:
				{
					required: 'Student is required'
				},
                amount:
				{
					required: 'Amount is required'
				},
                balance:
				{
					required: 'Balance is required'
				}
                  ,
                role:
				{
					required: 'Role is required'
				}

			},					
			
			errorPlacement: function(error, element)
			{
				error.insertAfter(element.parent());
			}
		});
		
 
 // Validation for order form
		$("#acount-infor").validate(
		{					
			rules:
			{	
				email:
				{
					required: true,
					email: true
				},
				phoneno:
				{
					required: true
				},
				password:
				{
					required: true,
					minlength: 3,
					maxlength: 20
				},
				confarmpassword:
				{
					required: true,
					minlength: 3,
					maxlength: 20
				},
                rolename:
				{
                  required: true
				}
			},
			messages:
			{	
			
				email:
				{
					required: 'Please enter your email address',
					email: 'Please enter a VALID email address'
				},
				phoneno:
				{
					required: 'Please enter mobile number'
				},
				password:
				{
					required: 'Please enter your password'
				},
				confarmpassword:
				{
					required: 'Please enter your confarm password'
				},
				rolename:
				{
					required: 'Role is required'
				}
				
			},					
			
			errorPlacement: function(error, element)
			{
				error.insertAfter(element.parent());
			}
		});
 
 // Validation for order form
		$(".addcourse").validate(
		{					
			rules:
			{	
				coursename:
				{
					required: true
				},
				finish:
				{
					required: true
				},
				duration:
				{
					required: true
				},
				price:
				{
					required: true
				},
				imageico:
				{
					required: true
				},
				department:
				{
					required: true
				},
				description:
				{
					required: true
				},
				crprofessor:
				{
					required: true
				},
				year:
				{
					required: true
				},
				email:
				{
					required: true,
					email: true
				},
				phoneno:
				{
					required: true
				},
				password:
				{
					required: true,
					minlength: 3,
					maxlength: 20
				},
				confarmpassword:
				{
					required: true,
					minlength: 3,
					maxlength: 20
				},
				rolename:
				{
                  required: true

				}
			},
			messages:
			{	
				coursename:
				{
					required: 'Please enter course name'
				},
				finish:
				{
					required: 'Please select date of birth'
				},
				duration:
				{
					required: 'Please enter duration'
				},
				price:
				{
					required: 'Please enter price'
				},
				imageico:
				{
					required: 'Please enter image'
				},
				department:
				{
					required: 'Please enter department'
				},
				description:
				{
					required: 'Please enter description'
				},
				crprofessor:
				{
					required: 'Please enter course professor'
				},
				year:
				{
					required: 'Please enter year'
				},
				email:
				{
					required: 'Please enter your email address',
					email: 'Please enter a VALID email address'
				},
				phoneno:
				{
					required: 'Please enter mobile number'
				},
				password:
				{
					required: 'Please enter your password'
				},
				confarmpassword:
				{
					required: 'Please enter your confarm password'
				},
				rolename:
				{
					required: 'Role name is required'
				}
				
			},					
			
			errorPlacement: function(error, element)
			{
				error.insertAfter(element.parent());
			}
		});
		
		
		
		
 
	// Validation for login form
		$("#comment").validate(
		{					
			rules:
			{	
				name:
				{
					required: true
				},
				message:
				{
					required: true
				},
				email:
				{
					required: true,
					email: true
				}
			},
			messages:
			{	
				name:
				{
					required: 'Please enter your name'
				},
				message:
				{
					required: 'Please enter your message'
				},
				email:
				{
					required: 'Please enter your email address',
					email: 'Please enter a VALID email address'
				}
			},					
			
			errorPlacement: function(error, element)
			{
				error.insertAfter(element.parent());
			}
		});
		
		
	// Validation for login form
		$(".addlibrary").validate(
		{					
			rules:
			{	
				nameasset:
				{
					required: true
				},
				subject:
				{
					required: true
				},
				imageico:
				{
					required: true
				},
				type:
				{
					required: true
				},
				price:
				{
					required: true
				},
				year:
				{
					required: true
				},
				status:
				{
					required: true
				},
				department:
				{
					required: true
				},
				email:
				{
					required: true,
					email: true
				}
			},
			messages:
			{	
				nameasset:
				{
					required: 'Please enter your name of assets'
				},
				subject:
				{
					required: 'Please enter your subject'
				},
				imageico:
				{
					required: 'Please enter image'
				},
				department:
				{
					required: 'Please enter your department'
				},
				type:
				{
					required: 'Please enter library type'
				},
				price:
				{
					required: 'Please enter price'
				},
				year:
				{
					required: 'Please enter year'
				},
				status:
				{
					required: 'Please enter status'
				},
				email:
				{
					required: 'Please enter your email address',
					email: 'Please enter a VALID email address'
				}
			},					
			
			errorPlacement: function(error, element)
			{
				error.insertAfter(element.parent());
			}
		});
		
	// Validation for login form
		$(".add-department").validate(
		{					
			rules:
			{	
				name:
				{
					required: true
				},
				headofdepartment:
				{
					required: true
				},
				email:
				{
					required: true
				},
				phone:
				{
					required: true
				},
				noofstudent:
				{
					required: true
				},
				status:
				{
					required: true
				}
			},
			messages:
			{	
				name:
				{
					required: 'Please enter your name'
				},
				headofdepartment:
				{
					required: 'Please enter head of department'
				},
				email:
				{
					required: 'Please enter email'
				},
				phone:
				{
					required: 'Please enter your phone'
				},
				noofstudent:
				{
					required: 'Please enter no of student'
				},
				status:
				{
					required: 'Please enter status'
				}
			},					
			
			errorPlacement: function(error, element)
			{
				error.insertAfter(element.parent());
			}
		});
		
	// Validation for login form
		$("#send-mail").validate(
		{					
			rules:
			{	
				name:
				{
					required: true
				},
				headofdepartment:
				{
					required: true
				},
				email:
				{
					required: true,
					email: true
				},
				phone:
				{
					required: true
				},
				noofstudent:
				{
					required: true
				},
				status:
				{
					required: true
				}
			},
			messages:
			{	
				name:
				{
					required: 'Please enter your name'
				},
				headofdepartment:
				{
					required: 'Please enter head of department'
				},
				email:
				{
					required: 'Please enter your email address',
					email: 'Please enter a VALID email address'
				},
				noofstudent:
				{
					required: 'Please enter no of student'
				},
				status:
				{
					required: 'Please enter status'
				}
			},					
			
			errorPlacement: function(error, element)
			{
				error.insertAfter(element.parent());
			}
		});


		
 
})(jQuery); 