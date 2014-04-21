Date: 2014-04-20 22:30
Title: Codename: "Flappy Drone"
Tags: quadcopters, rc, electronics
Slug: codename_flappy_drone
Author: Chris Gibson
Header: Chronicling my initial foray into the world of multi-rotors.
Summary: Building a multi-rotor from scratch means I can easily replace broken components without breaking the bank. It also means I can hand-pick the pieces to meet my purposes _(acrobatics, FPV, arial photography, etc...)_. At first, I was eying components that put the copter into the $600-$700, however it has become increasingly apparent to me that one can create a reliable and performant quadcopter for $200 or less, if you know where to look.

Building a quadcopter as a personal project. While the over-the-shelf options are entertaining _(The [Blade Nano Qx][nano_qx] is a great indoor nanocopter)_, any serious model is far too expensive and not easily modifiable.

Building a multi-rotor from scratch means I can easily replace broken components without breaking the bank. It also means I can hand-pick the pieces to meet my purposes _(acrobatics, FPV, arial photography, etc...)_. At first, I was eying components that put the copter into the $600-$700, however it has become increasingly apparent to me that one can create a reliable and performant quadcopter for $200 or less, if you know where to look.
* * *
### Current Build

| | | |
| --- | --- | ---: |
| __Frame:__ | [HobbyKing Q450][frame] | $15 |
| __Flight Controller:__ | [MultiWii Pro w/GPS][flight_controller] | $65 |
| __Motors:__ | [SunnySky 1260Kv][motors] (4x) |  $18 |
| __Speed Controllers:__ | [DYS SimonK Program 30A ESCs][esc] (4x) | $14 |
| __Battery:__ | [Glacier 30C 2200mAh][battery] | $22 |
| __Transmitter/Receiver:__ | [Turnigy 9X][transmitter] | $65 |
| __Props:__ | [GemFan 8x4.5][gemfan] | $2 |

<br/>
In total, after buying the above components (along with a soldering iron, LiPo charger, and a half-dozen other components) I was set back about $450. I didn't buy the cheapest parts, you could drop the cost down another $50-$100 if you worked at it. However, compared to the over-the-counter devices, you'll be flying around with more money in your wallet.

The Q450 frame is simply a clone of the more expensive DJI 450. I'm planning on upgrading to another more FPV-friendly frame _(perhaps the [Hoverthings Flip FPV][flip_fpv])_ and keeping the current one for testing and acrobatics.

I will post more information as the build progresses. Until that time, here's some other parts I reviewed during my search along with first impressions:
* * *
### Other Flight Controllers
There are several other flight controllers that are worth mentioning. The MultiWii was simply the cheapest for what I wanted, but each has its own set of advantages:

 __[KK 2.1.5][kk215]__ ($30)
 
* Includes an on-board display for easy modification on the field
* Lacks GPS support

__[CC3D][cc3d]__ ($90)

* Small, performant.
* Supposedly well built for acrobatic flying.

__[NAZA v2][naza]__ ($300)

* Professional grade, built for better automated flying.
* Has ecosystem for various addons (bluetooth controls, GPS, etc...)

__[MultiWii Pro][flight_controller]__ ($30-$70)

* Various styles. Flexible.
* Includes better sensors (barometer, 6-axis accelerometer, magnetometer, etc...)

### Notable Frames

 * [Hoverthings Flip FPV][flip_fpv] ($150)
 * [Lumeniere QAV400][qav400] ($165)
 * [TBS Discovery][tbs] ($74)
 * [Iconic-X][iconicx] ($145)

### More Resources

 * [Buddy RC][buddyrc]
 * [HobbyKing][hobbyking] _(Cheaper parts/clones from China)_
 * [GetFPV.com][getfpv]
 * [RCDude.com][rcdude]

* * *
_Please note I am an absolute ameteur at all this. This is just a record of my experiences. Please don't use the information I post as ground truth. Also, if you find any information on this post is in error, feel free to call me out in the comments below, I would really appreciate it!_
* * *

[naza]: http://www.hobbyking.com/hobbyking/store/__51633__dji_naza_m_v2_multi_rotor_flight_controller_gps_combo.html
[cc3d]: http://www.getfpv.com/openpilot-cc3d-flight-controller.html
[kk215]: http://www.hobbyking.com/hobbyking/store/__54299__Hobbyking_KK2_1_5_Multi_rotor_LCD_Flight_Control_Board_With_6050MPU_And_Atmel_644PA.html
[iconicx]: http://quadcopter.us/store/index.php?id_product=8&controller=product
[tbs]: http://team-blacksheep.com/shop/cat:discovery
[qav400]: http://www.getfpv.com/featured/qav400-frame-aluminum.html
[flip_fpv]: http://www.hoverthings.com/flipfpvproblack.html
[gemfan]: http://www.buddyrc.com/catalogsearch/result/?q=GemFan+8x4.5+
[rcdude]: http://www.rcdude.com/servlet/StoreFront
[getfpv]: http://www.getfpv.com/
[buddyrc]: http://www.buddyrc.com/
[hobbyking]: https://www.hobbyking.com
[nano_qx]: http://www.horizonhobby.com/products/nano-qx-bnf-with-safe-technology-BLH7680
[frame]: http://www.hobbyking.com/hobbyking/store/uh_viewitem.asp?idproduct=54664 
[flight_controller]: https://www.hobbyking.com/hobbyking/store/__26588__MultiWii_PRO_Flight_Controller_w_MTK_GPS_Module.html
[motors]: http://www.buddyrc.com/sunnysky-x2208-15-1260kv.html
[esc]: http://www.buddyrc.com/dys-simon-k-program-30a-multirotor-esc.html
[battery]: http://www.buddyrc.com/glacier-30c-2200mah-3s1p-t-plug.html
[transmitter]: https://www.hobbyking.com/hobbyking/store/__19673__Turnigy_9X_9Ch_Transmitter_w_Module_8ch_Receiver_Mode_2_v2_Firmware_USA_Warehouse_.html
