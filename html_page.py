success_setting_schedule = """\
<!DOCTYPE html>
<html style="font-size: 16px;" lang="ru"><head>
<meta charset="utf-8">
<title>Время установлено</title>
<style>
	.button-container {
	  text-align: center;
	  margin-top: 20px;
	  margin-right: 40px;
	}

	.button-container button {
	  padding: 10px 30px;
	  background-color: #478ac9;
	  color: #ffffff;
	  border: none;
	  cursor: pointer;
	  font-size: 16px;
	  text-decoration: none;
	  margin: 10px 0;
	  box-sizing: border-box;
	}
</style>
</head>
  <div class="u-clearfix u-sheet u-sheet-1" style="margin-right: 50px; margin-top: 500px">
	<div class="u-form u-form-1" style="text-align: center">
		<h2>Время работы с %s по %s</h2>
	</div>
  </div>
	<div class="button-container">
	  <button onclick="location.href='/'" id="return">Вернуться в главное меню</button>
	</div>
</html>
"""

set_time_page = """\
<!DOCTYPE html>
<html style="font-size: 16px;" lang="ru">
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta charset="utf-8">
  <title>Установка времени</title>
  <style>
    .u-input {
      display: block;
      width: 100%;
      padding: 10px 12px;
    }

    .u-btn {
      padding: 10px 30px;
      background-color: #478ac9;
      color: #ffffff;
    }

    .u-btn-submit {
      display: inline-block;
      margin: 1px;
    }

    .u-align-center {
      text-align: center;
    }

    a {
      text-decoration: none;
    }

    .u-form-control-hidden {
      display: none !important;
    }

    .u-overlap.u-overlap-transparent:not(.u-overlap-contrast) .u-header :not(.u-nav-item) > .u-btn,
    .u-gradient > .u-container-layout > .u-btn,
    .u-image:not(.u-shading) > .u-container-layout > .u-btn,
    .u-btn {
      background-color: #478ac9;
      color: #ffffff;
    }
  </style>
</head>
<body data-home-page="Главная.html" data-home-page-title="Главная" class="u-body u-xl-mode" data-lang="ru">
  <header class="u-clearfix u-header u-header" id="sec-b358">
    <div class="u-clearfix u-sheet u-sheet-1"></div>
  </header>
  <section class="u-clearfix u-section-1" id="sec-93b1">
    <div class="u-clearfix u-sheet u-sheet-1" style="margin-right: 50px">
      <div class="u-form u-form-1">
        <form action="/set-time" method="post" accept-charset="ISO-8859-1" class="u-clearfix u-form-spacing-10 u-form-vertical u-inner-form" name="form" style="padding: 10px;">
          <div class="u-form-date u-form-group u-form-partition-factor-2 u-form-group-6" style="margin: auto; width: 45%; height: 100px;">
            <label for="date-52ee" class="u-label">Установить время</label>
            <input type="time" id="date-52ee" name="input6" class="u-border-1 u-border-grey-30 u-input u-input-rectangle u-white" required="">
          </div>
          <div class="u-align-center u-form-group u-form-submit">
            <button class="u-btn u-btn-submit u-button-style" type="submit">Сохранить</button>
            <input type="submit" value="Сохранить" class="u-form-control-hidden">
          </div>
        </form>
      </div>
    </div>
  </section>
</body>
</html>
"""

success_set_time = """\
<!DOCTYPE html>
<html style="font-size: 16px;" lang="ru"><head>
<meta charset="utf-8">
<title>Время установлено</title>
<style>
	.button-container {
	  text-align: center;
	  margin-top: 20px;
	  margin-right: 40px;
	}

	.button-container button {
	  padding: 10px 30px;
	  background-color: #478ac9;
	  color: #ffffff;
	  border: none;
	  cursor: pointer;
	  font-size: 16px;
	  text-decoration: none;
	  margin: 10px 0;
	  box-sizing: border-box;
	}
</style>
</head>
  <div class="u-clearfix u-sheet u-sheet-1" style="margin-right: 50px; margin-top: 500px">
	<div class="u-form u-form-1" style="text-align: center">
		<h2>Время установлено</h2>
	</div>
  </div>
	<div class="button-container">
	  <button onclick="location.href='/'" id="return">Вернуться в главное меню</button>
	</div>
</html>
"""




home_page = """
<!DOCTYPE html>
<html style="font-size: 16px;" lang="ru">
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta charset="utf-8">
  <title>Главная</title>
  <style>
    body {
      background-color: #f5f5f5;
      color: #333333;
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
    }
    h4 {
      color: #333333;
      font-size: 18px;
      font-weight: bold;
    }

    .container {
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
    }

    .form-group {
      margin-bottom: 20px;
    }

    .form-group label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }

    .form-group input[type="range"] {
      width: 100%%;
    }

    .form-group input[type="time"] {
      width: 100%%;
      padding: 10px 12px;
    }

    .radio-group {
      margin-top: 10px;
    }

    .radio-group label {
      margin-right: 10px;
      display: inline-block;
      vertical-align: middle;
    }

	.button-container {
	  text-align: center;
	  margin-top: 20px;
	}

	.button-container button {
	  display: block;
	  width: 100%%;
	  padding: 10px 30px;
	  background-color: #478ac9;
	  color: #ffffff;
	  border: none;
	  cursor: pointer;
	  font-size: 16px;
	  text-decoration: none;
	  margin: 10px 0;
	  box-sizing: border-box;
	}

	.settings-button {
	  display: block;
	  padding: 10px 30px;
	  background-color: #478ac9;
	  color: #ffffff;
	  border: none;
	  cursor: pointer;
	  font-size: 16px;
	  text-decoration: none;
	  margin-bottom: 10px;
	  box-sizing: border-box;
	}

  </style>

  </style>
</head>
<body>
  <section>
    <div class="container">
      <div style="display: flex; align-items: center;">
        <a href="/settings" class="settings-button">Настройки</a>
        <h4 style="margin-left: auto;">Текущее время - %s</h4>
      </div>
      <form action="/" method="post" accept-charset="ISO-8859-1">
        <div class="form-group">
          <label for="input7">Рассвет/закат</label>
          <div class="radio-group">
            <input type="radio" id="input7" name="input7" value="on" required>
            <label for="input7">вкл</label>
            <input type="radio" id="input8" name="input7" value="off">
            <label for="input8">выкл</label>
          </div>
        </div>
        <div class="form-group">
          <label for="input8">Режим свечения</label>
          <div class="radio-group">
            <input type="radio" id="input9" name="input8" value="time" checked>
            <label for="input9">Ручной</label>
            <input type="radio" id="input10" name="input8" value="mode">
            <label for="input10">Автоматический</label>
          </div>
        </div>
        <div class="form-group">
          <label for="input1">1</label>
          <input type="range" id="input1" name="input1" min="-900" max="0" step="1" required>
        </div>
        <div class="form-group">
          <label for="input2">2</label>
          <input type="range" id="input2" name="input2" min="-900" max="0" step="1" required>
        </div>
        <div class="form-group">
          <label for="input3">3</label>
          <input type="range" id="input3" name="input3" min="-900" max="0" step="1" required>
        </div>
        <div class="form-group">
          <label for="input4">4</label>
          <input type="range" id="input4" name="input4" min="-900" max="0" step="1" required>
        </div>
        <div class="form-group">
          <div style="float: left; width: 45%%; height: 100px;">
            <label for="input5">Время с</label>
            <input type="time" id="input5" name="input5" required>
          </div>
          <div id="time-field" style="float: right; width: 45%%; height: 100px; display: block;">
            <label for="input6">Время до</label>
            <input type="time" id="input6" name="input6">
          </div>
        </div>
        <div id="mode-field" class="form-group" style="text-align: end; display: none;">
          <label for="input10">Режим свечения</label>
          <div class="radio-group">
            <input type="radio" id="input11" name="input10" value="18">
            <label for="input11">Вегетатика</label><br>
            <input type="radio" id="input12" name="input10" value="12">
            <label for="input12">Цветение</label>
          </div>
        </div>
        <div class="button-container">
          <button type="submit" id="save-button">Сохранить</button>
        </div>
      </form>
    </div>
  </section>
  <script>
    var timeRadio = document.querySelector('input[name="input8"][value="time"]');
    var modeRadio = document.querySelector('input[name="input8"][value="mode"]');
    var timeField = document.getElementById('time-field');
    var modeField = document.getElementById('mode-field');
    var vegetationRadio = document.getElementById('input11');
    var floweringRadio = document.getElementById('input12');
    var saveButton = document.getElementById('save-button');

    function updateRequired() {
      if (timeRadio.checked) {
        document.getElementById('input6').required = true;
        document.getElementById('input11').required = false;
        document.getElementById('input12').required = false;
      } else if (modeRadio.checked) {
        document.getElementById('input6').required = false;
        document.getElementById('input11').required = true;
        document.getElementById('input12').required = true;
      }
    }

    timeRadio.addEventListener('change', function() {
      timeField.style.display = 'block';
      modeField.style.display = 'none';
      updateRequired();
    });

    modeRadio.addEventListener('change', function() {
      timeField.style.display = 'none';
      modeField.style.display = 'block';
      updateRequired();

      if (modeRadio.checked) {
        document.getElementById('input6').value = '';
        document.getElementById('input11').checked = false;
        document.getElementById('input12').checked = false;
      }
    });

    vegetationRadio.addEventListener('change', function() {
      saveButton.disabled = false;
    });

    floweringRadio.addEventListener('change', function() {
      saveButton.disabled = false;
    });

    updateRequired();
  </script>
</body>
</html>
"""

settings_page = """\
<!DOCTYPE html>
<html style="font-size: 16px;" lang="ru">
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta charset="utf-8">
  <title>Настройки</title>
  <style>
    body {
      background-color: #f5f5f5;
      color: #333333;
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
    }
    h4 {
      color: #333333;
      font-size: 18px;
      font-weight: bold;
      margin-left: auto;
    }

    .container {
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
      display: flex;
      flex-direction: column; /* Изменено на вертикальное расположение элементов */
      align-items: center;
    }

    .form-group {
      margin-bottom: 20px;
    }

    .form-group label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }

    .form-group input[type="range"] {
      width: 100%%;
    }

    .form-group input[type="time"] {
      width: 100%%;
      padding: 10px 12px;
    }

    .radio-group {
      margin-top: 10px;
    }

    .radio-group label {
      margin-right: 10px;
      display: inline-block;
      vertical-align: middle;
    }

    .button-container {
      text-align: center;
      margin-top: 20px;
    }

    .button-container button,
    .button-container a {
      display: block;
      width: 300px; /* Изменено на фиксированную ширину */
      height: 40px;
      line-height: 40px;
      padding: 0;
      background-color: #478ac9;
      color: #ffffff;
      border: none;
      cursor: pointer;
      font-size: 16px;
      text-decoration: none;
      margin: 10px auto; /* Изменено на автоматическое выравнивание по горизонтали */
      box-sizing: border-box;
    }

    .settings-button {
      display: block;
      background-color: #478ac9;
      color: #ffffff;
      border: none;
      cursor: pointer;
      font-size: 12px;
      text-decoration: none;
      margin-bottom: 10px;
      box-sizing: border-box;
      height: 40px;
      line-height: 40px;
    }

    .main-menu-button {
      display: block;
      background-color: #478ac9;
      color: #ffffff;
      border: none;
      cursor: pointer;
      font-size: 14px;
      text-decoration: none;
      box-sizing: border-box;
      height: 40px;
      line-height: 40px;
    }

  </style>
</head>
<body>
  <section>
    <div class="container">
      <h4>Текущее время - %s</h4>
      <div class="button-container">
        <a href="/set-time" class="main-menu-button">Установить время</a>
      </div>
      <form action="/settings" method="post" accept-charset="ISO-8859-1">
        <div class="button-container">
          <button type="submit" id="save-button">Сбросить настройки освещения</button>
        </div>
      </form>

      <div class="button-container">
        <a href="/" class="main-menu-button">Главное меню</a>
      </div>
    </div>
  </section>
</body>
</html>


"""


success_reset_settings = """\
<!DOCTYPE html>
<html style="font-size: 16px;" lang="ru"><head>
<meta charset="utf-8">
<title>Сброс настроек</title>
<style>
	.button-container {
	  text-align: center;
	  margin-top: 20px;
	  margin-right: 40px;
	}

	.button-container button {
	  padding: 10px 30px;
	  background-color: #478ac9;
	  color: #ffffff;
	  border: none;
	  cursor: pointer;
	  font-size: 16px;
	  text-decoration: none;
	  margin: 10px 0;
	  box-sizing: border-box;
	}
</style>
</head>
  <div class="u-clearfix u-sheet u-sheet-1" style="margin-right: 50px; margin-top: 500px">
	<div class="u-form u-form-1" style="text-align: center">
		<h2>Настройки освещения сброшены</h2>
	</div>
  </div>
	<div class="button-container">
	  <button onclick="location.href='/'" id="return">Вернуться в главное меню</button>
	</div>
</html>
"""