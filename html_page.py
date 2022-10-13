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
<body data-home-page="Главная.html" data-home-page-title="Главная" class="u-body u-xl-mode" data-lang="ru"><header class="u-clearfix u-header u-header" id="sec-b358"><div class="u-clearfix u-sheet u-sheet-1"></div></header>
<section class="u-clearfix u-section-1" id="sec-93b1">
  <div class="u-clearfix u-sheet u-sheet-1" style="margin-right: 50px">
  <div style="text-align: right">Текущее время - %s</div>
	<div class="u-form u-form-1">
	  <form action="/test2" method="post" accept-charset="ISO-8859-1" class="u-clearfix u-form-spacing-10 u-form-vertical u-inner-form" name="form" style="padding: 10px;">
		<div class="u-form-date u-form-group u-form-group-1">
		  <label class="u-label">1</label>
		  <input type="range" name="input1" min="0" max="1023" step="1" class="u-border-1 u-border-grey-30 u-input u-input-rectangle u-white" required="">
		</div>
		<div class="u-form-date u-form-group u-form-partition-factor-2 u-form-group-5" style="float: left; width: 45%%; height: 100px;">
		  <label for="date-fcba" class="u-label u-label-5">Время с</label>
		  <input type="time" id="date-fcba" name="input5" class="u-border-1 u-border-grey-30 u-input u-input-rectangle u-white" required="">
		</div>
		<div class="u-form-date u-form-group u-form-partition-factor-2 u-form-group-6" style="float: right; width: 45%%; height: 100px;">
		  <label for="date-52ee" class="u-label">Время до</label>
		  <input type="time" id="date-52ee" name="input6" class="u-border-1 u-border-grey-30 u-input u-input-rectangle u-white" required="">
		</div>
		<div class="u-align-center u-form-group u-form-submit" style="margin-top: 5%%;">
		  <button class="u-btn u-btn-submit u-button-style" type="submit">Сохранить</button>
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
		<h2>Время работы ламп с %s по %s</h2>
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