// $('#submit').on('click', () => {
//     $.ajax({
//         type : "POST",
//         url : "https://api.stibee.com/v1/lists/81111/subscribers",
//         beforeSend: function (xhr) {
//             xhr.setRequestHeader("Content-type","application/json");
//             xhr.setRequestHeader("AccessToken","ed00b5b09dc81a0ee29ae26577bed3c2d5f38e5caedd824fe905ff5c6d9cbd4d6c8a79f45cb4641f9d54f4de85e713c83d6e50524343bd1fd4049e91d064175d");
//             xhr.setRequestHeader("listID", "81111");
//         },
//         data : {
//                 "eventOccuredBy": "MANUAL",
//                 "confirmEmailYN": "N",
//                 "groupIds": [
//                 ],
//                 "subscribers": [
//                     {
//                     "email": "lsm3191@naver.com",
//                     "name": "이수민",
//                     }
//                     ]
//                 },
//         success: function(response) { 
//         console.log(response);
//         },
//         error: function(response, status, error) {
//         console.log(response, status, error);
//         },
//         complete: function(response) {
//         console.log(response);
//         },
//     });
// });