// 캔버스 태그와 캔버스 컨텍스트를 가져옵니다.
var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");

// 오디오 태그를 가져옵니다.
var audio = document.querySelector("audio");

// 오디오 컨텍스트를 생성합니다.
var audioContext = new AudioContext();
var source = audioContext.createMediaElementSource(audio);
var analyser = audioContext.createAnalyser();

// 오디오 컨텍스트와 오디오 태그를 연결합니다.
source.connect(analyser);
analyser.connect(audioContext.destination);

// FFT 크기를 설정합니다.
analyser.fftSize = 2048;
var bufferLength = analyser.frequencyBinCount;
var dataArray = new Uint8Array(bufferLength);

// 캔버스 크기를 설정합니다.
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// 캔버스 중심 위치를 구합니다.
var centerX = canvas.width / 2;
var centerY = canvas.height / 2;

// 캔버스 반지름을 구합니다.
var radius = Math.min(canvas.width, canvas.height) / 2;

// 캔버스에 그리기 함수를 정의합니다.
function draw() {
  requestAnimationFrame(draw);

  analyser.getByteFrequencyData(dataArray);

  ctx.fillStyle = "black";
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  var barWidth = (2 * Math.PI) / bufferLength;
  var barHeight;

  ctx.beginPath();
  ctx.moveTo(centerX, centerY);

  for (var i = 0; i < bufferLength; i++) {
    barHeight = dataArray[i] / 2;

    var angle = i * barWidth - Math.PI / 2;
    var x = centerX + radius * Math.cos(angle);
    var y = centerY + radius * Math.sin(angle);

    ctx.lineTo(x, y);
  }

  ctx.closePath();
  ctx.fillStyle = "rgb(255, 0, 0)";
  ctx.fill();
}

// 캔버스에 그리기 함수를 호출합니다.
draw();
