# SolidGoldMagikarp fishing

(WIP)

Earlier this year, on [LessWrong](https://www.lesswrong.com/posts/aPeJE8bSo6rAFoLqg/solidgoldmagikarp-plus-prompt-generation) a series of GPT-3 tokens were documented, which would consistently produce anomalous results.

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/v1675551031/mirroredImages/aPeJE8bSo6rAFoLqg/l8wxznzrya2s0ayrilnf.png)

However, these tokens no longer elicit unusual behavior in GPT-3.5-turbo, or GPT4. Are there new tokens that can do this?

This repo makes an attempt to find them, but my conclusion is that there seemingly aren't any.

## Tokenizer status quo

https://github.com/openai/tiktoken/blob/main/tiktoken/model.py

This document indicates that the GPT3.5/GPT4 tokenizer is the same, and in fact, it is shared by the embeddings API! Hence - there's a rather convenient way to get embeddings for the same tokens.

## Approach

The current thesis for why these glitches exist in GPT-3, is that these tokens exist in the corpus used to train the tokenizer, but not in the one used to train the language model. Hence - the model behaves unpredictably because it's been given a token that it has never seen.

The method by Jessica & mwatkins describes two ways in which these anomalous tokens stick out:
- The anomalous tokens embed surprisingly close to the centroid of all possible GPT3 tokens.
- The anomalous tokens form their own special cluster, which is primarily composed of such tokens.

Additionally, consider the following 


```
Cluster 0
 [(" >;
 *=*= ().'/ }());
 //


 ]$ #${ ---
 ["_

Cluster 1
ámara enze ohana eea nge ustria ulen byname phem uden

Cluster 2
 WriteLine  Connecting  paddingHorizontal _ING  $

  RegexOptions (Properties  Tubes  Forgotten  BBB

Cluster 3
 Pork  chlorine  ecommerce  Borough  treadmill .smtp  myocard  tariff  scars  Cherokee

Cluster 4
ointed ,no ultimo .isDefined Regarding olvency >We -done -blind .HasPrefix

Cluster 5
 aktual  McInt  nues  phosphory  Obst  AUG  Paw  capit  Illum  NU

Cluster 6
033 303 290 238 679 093 786 938 979 088

Cluster 7
upply @update   ctrl decay dropout .ReadToEnd .Peek classify _Off implement

Cluster 8
 Gobierno  Suzanne  García  YM  Orbit  BDSM  Hanna  UClass  Garr Jacob

Cluster 9
FILENAME  craftsmanship PostalCodesNL urgery .getProduct _userid >Welcome Clark .surname Rail

Cluster 10
 temas  selber  se  meisten  neben  že  bleibt  daß  jede  einzel

Cluster 11
 molded  searchString  repost  populous  disclosing  tempting  remarked  soak  recomend  repair

Cluster 12
TestData -outs _graphics Regs ENSIONS DEPTH     names /fixtures .numberOfLines \Modules

Cluster 13
메 反 先 Ú  О 고 付 еш ה 路

Cluster 14
[color (protocol 'icon (anchor .BigInteger .leadingAnchor nextInt  UNSIGNED .histogram .clf

Cluster 15
 drifting  tacos  uterus /banner  timings /tty  micron .sms  fishes  alloys

Cluster 16
 dizzy  indifference  ubuntu  powerless  sophistication  quotas  mutated  extradition  jig  europé

Cluster 17
 kappa  mrb  vg  Vend  PHI  pł  pyt  garn  Hep  rq

Cluster 18
        ns prs _TXT št SWG _nh (sq xmax fdb PJ

Cluster 19
Bei $PostalCodesNL Desde (contract ourke _Parameter lund logan -vers unakan
```