<?php
namespace NethServer\Module\Dashboard\Applications;
class OMD extends \Nethgui\Module\AbstractModule implements \NethServer\Module\Dashboard\Interfaces\ApplicationInterface
{
  public function getName()
  {
    return "OMD";
  }
  public function getInfo()
  {
    $host = explode(':',$_SERVER['HTTP_HOST']);
    return array(
      'url' => "https://".$host[0]."/omd",
    );
  }
}
