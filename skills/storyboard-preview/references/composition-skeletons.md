# 构图骨架（SVG）

五种常用构图的 SVG 骨架，按 16:9 画。先按当前镜头确定机位、主体落位、遮挡和明暗，画面关系相符时取用合适的部分，其他构图按当前镜头另画；竖屏或方屏按同样的关系重新排布，不直接裁切。怎么画、画完怎么查，见 [构图小样](composition-sketch.md)。

## 逆光剪影

主体是暗的，背后满屏虚光，只有一道暖色轮廓光。

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 1000">
  <defs><clipPath id="f"><rect width="1600" height="900"/></clipPath></defs>
  <g id="frame" clip-path="url(#f)">
    <rect width="1600" height="900" fill="#1d1a1c"/>                          <!-- 夜 -->
    <circle cx="300" cy="150" r="70" fill="#e8a050" opacity=".35"/>           <!-- 背景虚灯，大小不一 -->
    <circle cx="620" cy="300" r="55" fill="#e8a050" opacity=".3"/>
    <circle cx="900" cy="120" r="50" fill="#e8a050" opacity=".4"/>
    <circle cx="1350" cy="220" r="80" fill="#e8a050" opacity=".3"/>
    <rect y="480" width="1600" height="200" fill="#c98a44" opacity=".2"/>     <!-- 灯下被照亮的人流带 -->
    <circle cx="1140" cy="430" r="40" fill="#0d0d10"/>                        <!-- 主体剪影，右三分 -->
    <path d="M1100 470 L1180 470 L1230 900 L1050 900 Z" fill="#0d0d10"/>
    <path d="M1180 470 L1230 900" stroke="#f0b060" stroke-width="4" fill="none"/> <!-- 暖色轮廓光 -->
    <ellipse cx="550" cy="650" rx="150" ry="380" fill="#0b0b0d" opacity=".65"/>   <!-- 前景虚掉的路人 -->
    <circle cx="80" cy="880" r="110" fill="#e07a2a" opacity=".45"/>           <!-- 左下火盆，被画框切掉 -->
  </g>
  <g id="labels" font-size="28" fill="#888"><text x="20" y="950">逆光剪影：主体是暗的，背后满屏虚光</text></g>
</svg>
```

## 框中框

画面大半是暗的门道或窗框，一块偏在一侧的亮口；主体是亮口前的小剪影。

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 1000">
  <defs><clipPath id="f"><rect width="1600" height="900"/></clipPath></defs>
  <g id="frame" clip-path="url(#f)">
    <rect width="1600" height="900" fill="#0e0e10"/>                          <!-- 暗的门道 -->
    <rect x="1000" y="260" width="300" height="480" fill="#5d7a9e"/>          <!-- 亮门口，偏右三分 -->
    <circle cx="1050" cy="520" r="14" fill="#e8a050"/>                        <!-- 门外的几点暖灯 -->
    <circle cx="1190" cy="500" r="10" fill="#e8a050"/>
    <circle cx="1260" cy="560" r="16" fill="#e8a050"/>
    <polygon points="1000,740 1300,740 1600,900 820,900" fill="#3a4a60" opacity=".55"/> <!-- 地上铺进来的冷光 -->
    <circle cx="1110" cy="560" r="16" fill="#0a0a0c"/>                        <!-- 主体：亮口前的小剪影 -->
    <polygon points="1090,578 1130,578 1145,740 1075,740" fill="#0a0a0c"/>
  </g>
  <g id="labels" font-size="28" fill="#888"><text x="20" y="950">框中框：暗门道里一块偏在一侧的亮门口</text></g>
</svg>
```

## 前景擦过

贴着镜头横穿的人虚成一大块，挡住画面中间；下一刻擦过去，画面变了（例如少了一个人）。擦过之后的样子另画一张。

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 1000">
  <defs><clipPath id="f"><rect width="1600" height="900"/></clipPath></defs>
  <g id="frame" clip-path="url(#f)">
    <rect width="1600" height="900" fill="#1b2029"/>
    <rect y="500" width="1600" height="400" fill="#24211e"/>                  <!-- 地面 -->
    <circle cx="200" cy="180" r="40" fill="#e8a050" opacity=".5"/>
    <circle cx="1400" cy="200" r="45" fill="#e8a050" opacity=".5"/>
    <circle cx="500" cy="320" r="38" fill="#e6e1d8"/>                         <!-- 左：浅色衣服的人 -->
    <polygon points="455,365 545,365 575,900 425,900" fill="#e6e1d8"/>
    <circle cx="1100" cy="310" r="40" fill="#2a2030"/>                        <!-- 右：深色衣服的人 -->
    <polygon points="1050,355 1150,355 1185,900 1015,900" fill="#2a2030"/>
    <ellipse cx="800" cy="560" rx="230" ry="520" fill="#120e10" opacity=".82"/> <!-- 前景擦过的人，只挡中间 -->
    <circle cx="780" cy="160" r="160" fill="#f0a040" opacity=".35"/>          <!-- 他手里的火把 -->
    <circle cx="780" cy="160" r="60" fill="#ffd27a" opacity=".55"/>
  </g>
  <g id="labels" font-size="28" fill="#888"><text x="20" y="950">前景擦过：虚掉的人只挡住两人中间</text></g>
</svg>
```

## 高机位斜线

屋檐斜切画面，柱子分开两人；地上的阴影线把一人放在光里、一人放在暗里。高机位往下看时，离镜头近的地面在画面下方，屋檐底下的深处在画面上方。

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 1000">
  <defs><clipPath id="f"><rect width="1600" height="900"/></clipPath></defs>
  <g id="frame" clip-path="url(#f)">
    <rect width="1600" height="900" fill="#8a7a64"/>                          <!-- 被阳光照到的地面 -->
    <polygon points="0,465 1600,225 1600,380 0,620" fill="#2c3442" opacity=".85"/> <!-- 屋檐下的阴影带 -->
    <polygon points="0,0 1600,0 1600,180 0,420" fill="#5a5d63"/>             <!-- 瓦顶，斜切画面上方 -->
    <polygon points="0,420 1600,180 1600,225 0,465" fill="#2a2a2e"/>          <!-- 檐口 -->
    <rect x="760" y="300" width="60" height="600" fill="#7a3b2a"/>            <!-- 柱子，把画面一分为二 -->
    <ellipse cx="560" cy="640" rx="75" ry="45" fill="#26301f"/>               <!-- 左：俯视的肩背，在光里 -->
    <circle cx="560" cy="585" r="30" fill="#141414"/>
    <path d="M490 650 Q560 690 630 650" stroke="#f0b060" stroke-width="4" fill="none"/>
    <polygon points="1010,300 1110,300 1115,450 1005,450" fill="#26301f" opacity=".9"/> <!-- 右：站得更深，头被檐挡住，在暗里 -->
  </g>
  <g id="labels" font-size="28" fill="#888"><text x="20" y="950">高机位斜线：阴影线把两人分在光里和暗里</text></g>
</svg>
```

## 大负空间里的小人

人只占画面高度的十分之一左右，放在三分线上；大片天空或空地本身就是情绪。提示词里要写明人很小，否则模型常把人放大。

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 1000">
  <defs><clipPath id="f"><rect width="1600" height="900"/></clipPath></defs>
  <g id="frame" clip-path="url(#f)">
    <rect width="1600" height="900" fill="#c9d3dc"/>                          <!-- 大片天空 -->
    <polygon points="0,560 300,520 700,545 1100,510 1600,540 1600,580 0,580" fill="#8e9aa6"/> <!-- 远山 -->
    <rect y="575" width="1600" height="40" fill="#6b6f75"/>                   <!-- 屋顶 -->
    <rect y="615" width="1600" height="155" fill="#2a2826"/>                  <!-- 廊下的暗带 -->
    <rect y="770" width="1600" height="130" fill="#9a948a"/>                  <!-- 地面 -->
    <circle cx="1070" cy="672" r="9" fill="#1a2a1e"/>                         <!-- 很小的人，右三分 -->
    <polygon points="1061,681 1079,681 1084,745 1056,745" fill="#1a2a1e"/>
    <polygon points="60,900 115,900 160,600 125,590" fill="#2a2420"/>         <!-- 画面边上的树，只露一部分 -->
    <circle cx="150" cy="560" r="60" fill="#f2efe8" opacity=".75"/>
    <circle cx="225" cy="610" r="40" fill="#f2efe8" opacity=".75"/>
    <circle cx="85" cy="515" r="50" fill="#f2efe8" opacity=".75"/>
  </g>
  <g id="labels" font-size="28" fill="#888"><text x="20" y="950">大负空间里的小人：人约占画面高度十分之一</text></g>
</svg>
```

