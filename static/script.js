let startFeedingButton = document.getElementById('startFeeding');
let stopFeedingButton = document.getElementById('stopFeeding');
let startEggButton = document.getElementById('startEgg');
let stopEggButton = document.getElementById('stopEgg');
let startWasteButton = document.getElementById('startWaste');
let stopWasteButton = document.getElementById('stopWaste');




let Button = document.getElementsByClassName('system-container');

let feedingProcess = 'stop';

startFeedingButton.addEventListener('click', function(){
    startFeedingButton.value = 1
    console.log("startFeedingButton:", startFeedingButton.value);
})
stopFeedingButton.addEventListener('click', function(){
    stopFeedingButton.value = 1
    console.log("stopFeedingButton:", stopFeedingButton.value);
})
startEggButton.addEventListener('click', function(){
    startEggButton.value = 1
    console.log("startEggButton:", startEggButton.value);
})
stopEggButton.addEventListener('click', function(){
    stopEggButton.value = 1;
    console.log("stopEggButton:", stopEggButton.value);
})
startWasteButton.addEventListener('click', function(){
    startWasteButton.value = 1;
    console.log("startWasteButton:", startWasteButton.value);
})
stopWasteButton.addEventListener('click', function(){
    stopWasteButton.value = 1;
    console.log("stopWasteButton:", stopWasteButton.value);
})
