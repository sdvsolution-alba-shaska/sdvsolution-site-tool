(function(){
  var f=document.getElementById('demoForm'), s=document.getElementById('demoStatus');
  if(!f) return;
  f.addEventListener('submit', function(e){
    e.preventDefault();
    s.style.color='#9AA8B4'; s.textContent='Sending your request.';
    fetch(f.action,{method:'POST',body:new FormData(f),headers:{'Accept':'application/json'}}).then(function(r){
      if(r.ok){ f.reset(); s.style.color='#9CFF3A'; s.textContent='Request sent. We will reply by email.'; }
      else { s.style.color='#FFB020'; s.textContent='The request was not sent. Check the email address and send it again.'; }
    }).catch(function(){ s.style.color='#FFB020'; s.textContent='The request was not sent because the connection dropped. Send it again.'; });
  });
})();
