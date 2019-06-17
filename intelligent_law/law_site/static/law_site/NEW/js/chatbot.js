function scrollModuleToBottom() {
  var chatModule = document.querySelector('.chat-module');
  chatModule.scrollTop = chatModule.scrollHeight;
}

// function sendInput() {

    $("#id-user-input").change(function () {
      toggleInput(false);
      
      console.log( $(this).val() );
      var user_message = $(this).val();

      $.ajax({
        url: '/ajax/get_bot_answer/',
        data: {
          'user_message': user_message
        },
        dataType: 'json',
        success: function (data) {
          var inputElt = document.querySelector('[data-role="user-input"]');
          if(inputElt.value == '')
            return;

          var thread = document.querySelector('.thread');
          var newThreadItem = createThreadItem(false);
          var responseItem = newThreadItem.querySelector('.response');
          responseItem.innerText = inputElt.value;
          thread.appendChild(newThreadItem);
          inputElt.value = '';
          scrollModuleToBottom();
          setTimeout(function() {
            showResponse(data.bot_answer);
          }, 200);
        }
      });

    });

// }

function createThreadItem(isBot) {
    var thread = document.querySelector('.thread');
    var threadItem = document.createElement('div');
    var avatarItem = document.createElement('div');
    var responseContainerItem = document.createElement('div');
    var responseItem = document.createElement('div');
    threadItem.classList.add('thread-item');
    avatarItem.classList.add('avatar-container');
    responseContainerItem.classList.add('response-container');
    responseItem.classList.add('response');
    responseContainerItem.appendChild(responseItem);
    threadItem.appendChild(avatarItem);
    threadItem.appendChild(responseContainerItem);
    thread.appendChild(threadItem);
    if (isBot) {
        avatarItem.appendChild(createBotAvatar());
    } else {
        threadItem.classList.add('user-item');
    }
    return threadItem;
}

function createBotAvatar() {
    // make previous avatar inactive
    var previousAvatar = document.querySelector('.calliope.idle:not(.big), .calliope.appearing:not(.big)');
    if (previousAvatar) {
        previousAvatar.classList.remove('idle');
        previousAvatar.classList.remove('appearing');
        previousAvatar.classList.add('inactive');
    }
    var calliopeItem = document.createElement('div');
    var headItem = document.createElement('div');
    var eyeLeftItem = document.createElement('div');
    var eyeRightItem = document.createElement('div');
    var torsoItem = document.createElement('div');
    var armLeftItem = document.createElement('div');
    var armRightItem = document.createElement('div');
    var feetItem = document.createElement('div');
    calliopeItem.classList.add('calliope');
    calliopeItem.classList.add('appearing');
    headItem.classList.add('head');
    eyeLeftItem.classList.add('eye-left');
    eyeRightItem.classList.add('eye-right');
    torsoItem.classList.add('torso');
    armLeftItem.classList.add('arm-left');
    armRightItem.classList.add('arm-right');
    feetItem.classList.add('feet');
    headItem.appendChild(eyeLeftItem);
    headItem.appendChild(eyeRightItem);
    torsoItem.appendChild(armLeftItem);
    torsoItem.appendChild(armRightItem);
    calliopeItem.appendChild(headItem);
    calliopeItem.appendChild(torsoItem);
    calliopeItem.appendChild(feetItem);
    return calliopeItem;
}

function showResponse(response) {
    var newThreadItem = createThreadItem(true);
    var responseItem = newThreadItem.querySelector('.response');
    scrollModuleToBottom();

    responseItem.innerHTML = response;
    var calliope = newThreadItem.querySelector('.calliope.appearing');
    calliope.classList.remove('appearing');
    calliope.classList.add('idle');

    toggleInput(true);
    manageChatOverlay();

}

function manageChatOverlay() {
    var overlay = document.querySelector('.scroll-overlay');
    var chatModule = document.querySelector('.chat-module');
    if (chatModule.scrollTop > 0) {
        overlay.classList.remove('overlay-hidden');
    } else {
        overlay.classList.add('overlay-hidden');
    }
}

function toggleInput(enabled) {
    var inputElement = document.querySelector('[data-role="user-input"]');
    inputElement.disabled = !enabled;
    if (enabled) {
        inputElement.focus();
    }
}
