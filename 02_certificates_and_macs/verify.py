
Modulus=0x00b6e02fc22406c86d045fd7ef0a6406b27d22266516ae42409bcedc9f9f76073ec330558719b94f940e5a941f5556b4c2022aafd098ee0b40d7c4d03b72c8149eef90b111a9aed2c8b8433ad90b0bd5d595f540afc81ded4d9c5f57b786506899f58adad2c7051fa897c9dca4b182842dc6ada59cc71982a6850f5e44582a378ffd35f10b0827325af5bb8b9ea4bd51d027e2dd3b4233a30528c4bb28cc9aac2b230d78c67be65e71b74a3e08fb81b71616a19d23124de5d79208ac75a49cbacd17b21e4435657f532539d11c0a9a631b199274680a37c2c25248cb395aa2b6e15dc1dda020b821a293266f144a2141c7ed6d9bf2482ff303f5a26892532f5ee3
Modulusr=0x00c6cce573e6fbd4bbe52d2d32a6dfe5813fc9cd2549b6712ac3d5943467a20a1cb05f69a640b1c4b7b28fd098a4a941593ad3dc94d63cdb7438a44acc4d2582f74aa5531238eef3496d71917e63b6aba65fc3a484f84f6251bef8c5ecdb3892e306e508910cc4284155fbcb5a89157e71e835bf4d72093dbe3a38505b77311b8db3c724459aa7ac6d00145a04b7ba13eb510a984141224e656187814150a6795c89de194a57d52ee65d1c532c7e98cd1a0616a46873d03404135ca171d35a7c55db5e64e13787305604e511b4298012f1793988a202117c2766b788b778f2ca0aa838ab0a64c2bf665d9584c1a1251e875d1a500b2012cc41bb6e0b5138b84bcb




Exponent = 65537
#Hash = 0x135c2a2d9142359d8a00fdb500c145d61badee5f32cf4b362d9aa54296a85c57
Signature = 0x188a958903e66ddf5cfc1d68ea4a8f83d6512f8d6b44169eac63f5d26e6c84998baa8171845bed344eb0b7799229cc2d806af08e20e179a4fe034713eaf586ca59717df404966bd359583dfed331255c183884a3e69f82fd8c5b98314ecd789e1afd85cb49aaf2278b9972fc3eaad5410bdad536a1bf1c6e47497f5ed9487c03d9fd8b49a098264240ebd69211a4640a5754c4f51dd6025e6baceec4809a1272fa5693d7ffbf30850630bf0b7f4eff57059d24ed85c32bfba675a8ac2d16ef7d7927b2ebc29d0b07eaaa85d301a3202841594328d281e3aaf6ec7b3b77b640628005414501ef17063edec0339b67d3612e7287e469fc120057401e70f51ec9b4
signaturer=0x1c1a0697dcd79c9f3c886606085721db2147f82a67aabf183276401057c18af37ad911658e35fa9efc45b59ed94c314bb891e8432c8eb378cedbe3537971d6e5219401da55879a2464f68a66ccde9c37cda834b1699b23c89e78222b7043e35547316119ef58c5852f4e30f6a0311623c8e7e2651633cbbf1a1ba03df8ca5e8b318b6008892d0c065c52b7c4f90a98d1155f9f12be7c366338bd44a47fe4262b0ac497690de98ce2c01057b8c876129155f24869d8bc2a025b0f44d42031dbf4ba70265d90609ebc4b17092fb4cb1e4368c90727c1d25cf7ea21b968129c3c9cbf9efc805c9b63cdec47aa252767a037f300827d54d7a9f8e92e13a377e81f4a


print(hex(pow(Signature, Exponent, Modulus)),"\n")
print(hex(pow(signaturer,Exponent,Modulusr)))