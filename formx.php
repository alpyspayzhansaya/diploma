<?php
if(isset($_SERVER['HTTP_X_REQUESTED_WITH']) && !empty($_SERVER['HTTP_X_REQUESTED_WITH']) && strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) == 'xmlhttprequest') //проверка на асинхронность
	{
    if (isset($_POST["name"]) && isset($_POST["email"]) && isset($_POST["id"]) && isset($_POST["phone"]) && isset($_POST["address"]) && isset($_POST["workplace"]) && isset($_POST["income"]) && isset($_POST["income-additional"]) 
		&& isset($_POST["trustworthy"]) && isset($_POST["trustworthy-phone"]) && isset($_POST["kinship-degree"]) )
 	{ 
    if ($_POST['name'] == '') 
    {
        echo 'Не заполнено поле Имя';
        return; //проверяем наличие обязательных полей
    }
	if ($_POST['id'] == '') 
    {
        echo 'Не указан ИИН';
        return; //проверяем наличие обязательных полей
    }
	if ($_POST['phone'] == '') 
    {
        echo 'Не указаны контакты';
        return; //проверяем наличие обязательных полей
    }
	if ($_POST['address'] == '') 
    {
        echo 'Не указан адрес проживания';
        return; //проверяем наличие обязательных полей
    }
	if ($_POST['workplace'] == '') 
    {
        echo 'Не указано рабочее место';
        return; //проверяем наличие обязательных полей
    }
	if ($_POST['income'] == '') 
    {
        echo 'Не указан основной доход';
        return; //проверяем наличие обязательных полей
    }
	if ($_POST['income-additional'] == '') 
    {
        echo 'Не указан дополнительный доход';
        return; //проверяем наличие обязательных полей
    }
	if ($_POST['trustworthy'] == '') 
    {
        echo 'Не указано доверительное лицо';
        return; //проверяем наличие обязательных полей
    }
	if ($_POST['trustworthy-phone'] == '') 
    {
        echo 'Не указан контакт доверительного лица';
        return; //проверяем наличие обязательных полей
    }
	if ($_POST['kinship-degree'] == '') 
    {
        echo ' Не указано степень родства';
        return; //проверяем наличие обязательных полей
    }
    if ($_POST['email'] == '') 
    {
        echo 'Не заполнено поле E-mail';
        return;
    } 
    $name = $_POST['name'];
    $email = $_POST['id'];
	$name = $_POST['phone'];
    $email = $_POST['address'];
	$name = $_POST['workplace'];
    $email = $_POST['income'];
	$name = $_POST['income-additional'];
    $email = $_POST['trustworthy'];
	$name = $_POST['trustworthy-phone'];
    $email = $_POST['kinship-degree'];
    $email = $_POST['email'];
        echo 'Заявка отправлена!';
    	
    }
    }
?>