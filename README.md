# 1999decrypt
重返未来1999资源文件解密

2023/5/30

正式版1.0.3加密与cb3相同

角色live2d的moc3文件位于Assets\ZResourcesLib\live2d\roles\角色id_角色名字\角色id_角色名字

资产类型为MonoBehaviour moc3数据在data中，可使用assetstudio dump raw 然后删去MonoBehaviour头部多余的数据

2024/4/9

加了几行代码支持并行，跑得快一点，加密文件放bundles里面，解密完成之后放在bundles-decrypt里面