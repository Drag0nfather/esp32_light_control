home_page = """\
<!DOCTYPE html>
<html style="font-size: 16px;" lang="ru"><head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta charset="utf-8">
<title>Главная</title>
<style>.u-input {display: block;width: 100%%;padding: 10px 12px;}</style>
<style>.u-btn {padding: 10px 30px;}</style>
<style>.u-btn-submit {display: inline-block; margin: 1px;}</style>
<style>.u-align-center {text-align: center;}</style>
<style>a {text-decoration: none;}</style>
<style>.u-form-control-hidden {display: none !important;}</style>
<style>.u-overlap.u-overlap-transparent:not(.u-overlap-contrast) .u-header :not(.u-nav-item) > .u-btn, .u-gradient > .u-container-layout > .u-btn, .u-image:not(.u-shading) > .u-container-layout > .u-btn, .u-btn {background-color: #478ac9;color: #ffffff;}</style>
</head>
<body data-home-page="Главная.html" data-home-page-title="Главная">
<section>
  <div style="margin-right: 50px">
	  <div style="text-align: right; margin-bottom: -3%%"><h4>Текущее время - %s</h4></div>
	<div>
	  <form action="/test2" method="post" accept-charset="ISO-8859-1" style="padding: 10px;">
		<div>
		  <label>1</label>
		  <input type="range" name="input1" min="-900" max="0" step="1" class="u-input" required="">
		</div>
		<div>
			<label>2</label>
			<input type="range" name="input2"  min="-900" max="0" step="1" class="u-input" required="">
		</div>
		<div>
			<label>3</label>
			<input type="range" name="input3" min="-900" max="0" step="1" class="u-input" required="">
		</div>
		<div>
			<label>4</label>
			<input type="range" name="input4"  min="-900" max="0" step="1" class="u-input" required="">
		</div>
		<div style="float: left; width: 45%%; height: 100px; margin-top: 1%%">
		  <label>Время с</label>
		  <input type="time" name="input5" class="u-input" required="">
		</div>
		<div style="float: right; width: 45%%; height: 100px; margin-top: 1%%">
		  <label>Время до</label>
		  <input type="time" name="input6" class="u-input" required="">
		<div class="u-input" style="text-align: right; margin-top: 2%%">
			<span title="Опция закат/рассвет добавит пол-часа к началу и концу свечения">Рассвет/закат</span>
            <br>
			<input type="radio" name="input7" value="on" required=""> <label for="input7">вкл</label>
			<input type="radio" name="input7" value="off"> <label for="input7">выкл</label>
		</div>
		</div>
		<div class="u-align-center" style="margin-top: 5%%" >
		  <button class="u-btn u-btn-submit" type="submit">Сохранить</button>
		  <input type="submit" value="Сохранить" class="u-form-control-hidden">
		</div>
	  </form>
	</div>
  </div>
</section>

</body></html>
"""


success_setting_schedule = """\
<!DOCTYPE html>
<html style="font-size: 16px;" lang="ru"><head>
<meta charset="utf-8">
<title>Время установлено</title>
</head>
  <div class="u-clearfix u-sheet u-sheet-1" style="margin-right: 50px">
	<div class="u-form u-form-1" style="text-align: center">
		<h2>Время работы с %s по %s</h2>
	</div>
  </div>
</html>
"""

set_time_page = """\
<!DOCTYPE html>
<html style="font-size: 16px;" lang="ru"><head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta charset="utf-8">
<title>Установка времени</title>
<style>.u-input {display: block;width: 100%%;padding: 10px 12px;}</style>
<style>.u-btn {padding: 10px 30px;}</style>
<style>.u-btn-submit {display: inline-block; margin: 1px;}</style>
<style>.u-align-center {text-align: center;}</style>
<style>a {text-decoration: none;}</style>
<style>.u-form-control-hidden {display: none !important;}</style>
<style>.u-overlap.u-overlap-transparent:not(.u-overlap-contrast) .u-header :not(.u-nav-item) > .u-btn, .u-gradient > .u-container-layout > .u-btn, .u-image:not(.u-shading) > .u-container-layout > .u-btn, .u-btn {background-color: #478ac9;color: #ffffff;}</style>
</head>
<body data-home-page="Главная.html" data-home-page-title="Главная" class="u-body u-xl-mode" data-lang="ru"><header class="u-clearfix u-header u-header" id="sec-b358"><div class="u-clearfix u-sheet u-sheet-1"></div></header>
<section class="u-clearfix u-section-1" id="sec-93b1">
  <div class="u-clearfix u-sheet u-sheet-1" style="margin-right: 50px">
	<div class="u-form u-form-1">
	  <form action="/set-time" method="post" accept-charset="ISO-8859-1" class="u-clearfix u-form-spacing-10 u-form-vertical u-inner-form" name="form" style="padding: 10px;">
		<div class="u-form-date u-form-group u-form-partition-factor-2 u-form-group-6" style="margin: auto; width: 45%%; height: 100px;">
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
</body></html>
"""

success_set_time = """\
<!DOCTYPE html>
<html style="font-size: 16px;" lang="ru"><head>
<meta charset="utf-8">
<title>Время установлено</title>
</head>
  <div class="u-clearfix u-sheet u-sheet-1" style="margin-right: 50px">
	<div class="u-form u-form-1" style="text-align: center">
		<h2>Время установлено</h2>
	</div>
  </div>
</html>
"""

main_page = """\
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width; initial-scale=1.0;">
    <title>Главная страница</title>
    <link rel="stylesheet" href="styles.css">
</head>
    <body>
        <div class="main_title">Система управления освещением</div>
        <a href="hand-set.html" class="button">Задать программу вручную</a>
        <a href="auto-set.html" class="button">Установить из заданных программ</a>
        <a href="set-time.html" class="button">Установить время</a>
        <div class="current_time">Текущее время - %s</div>
    </body>
</html>

"""

sheduled_time_page = """\
<!DOCTYPE html>
<html style="font-size: 16px;" lang="ru"><head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta charset="utf-8">
<title>Главная</title>
<style>.u-input {display: block;width: 100%%;padding: 10px 12px;}</style>
<style>.u-btn {padding: 10px 30px;}</style>
<style>.u-btn-submit {display: inline-block; margin: 1px;}</style>
<style>.u-align-center {text-align: center;}</style>
<style>a {text-decoration: none;}</style>
<style>.u-form-control-hidden {display: none !important;}</style>
<style>.u-overlap.u-overlap-transparent:not(.u-overlap-contrast) .u-header :not(.u-nav-item) > .u-btn, .u-gradient > .u-container-layout > .u-btn, .u-image:not(.u-shading) > .u-container-layout > .u-btn, .u-btn {background-color: #478ac9;color: #ffffff;}</style>
</head>
<body data-home-page="Главная.html" data-home-page-title="Главная">
<section>
  <div style="margin-right: 50px">
	  <div style="text-align: right; margin-bottom: -3%%"><h4>Текущее время - %s</h4></div>
	<div>
	  <form action="/schedule" method="post" accept-charset="ISO-8859-1" style="padding: 10px;">
		<div>
		  <label>1</label>
		  <input type="range" name="input1" min="-900" max="0" step="1" class="u-input" required="">
		</div>
		<div>
			<label>2</label>
			<input type="range" name="input2"  min="-900" max="0" step="1" class="u-input" required="">
		</div>
		<div>
			<label>3</label>
			<input type="range" name="input3" min="-900" max="0" step="1" class="u-input" required="">
		</div>
		<div>
			<label>4</label>
			<input type="range" name="input4"  min="-900" max="0" step="1" class="u-input" required="">
		</div>
		<div style="float: left; width: 45%%; height: 100px; margin-top: 1%%">
		  <label>Время начала</label>
		  <input type="time" name="input5" class="u-input" required="">
		</div>
		<div class="u-input" style="text-align: end; margin-top: 2%%">
			<span title="Вегетатика - 18 часов, цветение - 12 часов">Режим свечения</span>
            <br>
			<input type="radio" name="input7" value="18" required=""> <label for="input7">Вегетатика</label>
			<input type="radio" name="input7" value="12"> <label for="input7">Цветение</label>
		</div>
		</div>
		<div class="u-align-center" style="margin-top: 5%%" >
		  <button class="u-btn u-btn-submit" type="submit">Сохранить</button>
		  <input type="submit" value="Сохранить" class="u-form-control-hidden">
		</div>
	  </form>
	</div>
  </div>
</section>

</body></html>

"""
