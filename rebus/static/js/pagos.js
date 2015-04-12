
$(function(){



  $('#submit_pagos').on('submit', function(e){


    e.preventDefault();
    Conekta.setPublishableKey("key_CAniAetz1nboWvXz4MwCHEQ");


  var csrftoken = $('meta[name=csrftoken]').attr('content');
  var errorResponseHandler, successResponseHandler, tokenParams;
  var number = $("#number").val()
  var name = $("#name").val()
  var exp_year = $("#exp_year").val()
  var exp_month = $("#exp_month").val()
  var cvc = $("#cvc").val()

  tokenParams = {
    "card": {
      "number": number,
      "name": name,
      "exp_year": exp_year,
      "exp_month": exp_month,
      "cvc": cvc
    }
  };


  successResponseHandler = function(token) {

    return $.post('/token/', {token_id:token.id, csrfmiddlewaretoken: csrftoken} , function() {
      return document.location = 'payment_succeeded';
    });
  };

  errorResponseHandler = function(error) {
    return console.log(error.message);
  };


  Conekta.token.create(tokenParams, successResponseHandler, errorResponseHandler);
  });

  
})

