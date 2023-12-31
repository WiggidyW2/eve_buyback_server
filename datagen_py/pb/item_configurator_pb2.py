# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: item_configurator.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import weve_esi_pb2 as weve__esi__pb2
import buyback_pb2 as buyback__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17item_configurator.proto\x12\x17item_configurator_proto\x1a\x0eweve_esi.proto\x1a\rbuyback.proto\"\xef\x01\n\x08ListItem\x12\x0f\n\x07type_id\x18\x01 \x01(\r\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\x12@\n\x08json_idx\x18\x03 \x03(\x0b\x32..item_configurator_proto.ListItem.JsonIdxEntry\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x18\n\x10market_group_idx\x18\x05 \x01(\r\x12\x11\n\tgroup_idx\x18\x06 \x01(\r\x12\x14\n\x0c\x63\x61tegory_idx\x18\x07 \x01(\r\x1a.\n\x0cJsonIdxEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\"\xaf\x01\n\x07ListRep\x12\x30\n\x05items\x18\x01 \x03(\x0b\x32!.item_configurator_proto.ListItem\x12\x0c\n\x04json\x18\x02 \x03(\t\x12\x15\n\rmarket_groups\x18\x03 \x03(\t\x12\x0e\n\x06groups\x18\x04 \x03(\t\x12\x12\n\ncategories\x18\x05 \x03(\t\x12\x15\n\rrefresh_token\x18\x06 \x01(\t\x12\x12\n\nauthorized\x18\x07 \x01(\x08\"\xb0\x02\n\x07ListReq\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rrefresh_token\x18\x02 \x01(\t\x12\x37\n\x0finclude_enabled\x18\x03 \x01(\x0e\x32\x1e.item_configurator_proto.Query\x12:\n\x12include_configured\x18\x04 \x01(\x0e\x32\x1e.item_configurator_proto.Query\x12\x14\n\x0cinclude_json\x18\x05 \x01(\x08\x12\x10\n\x08language\x18\x06 \x01(\t\x12\x14\n\x0cinclude_name\x18\x07 \x01(\x08\x12\x1c\n\x14include_market_group\x18\x08 \x01(\x08\x12\x15\n\rinclude_group\x18\t \x01(\x08\x12\x18\n\x10include_category\x18\n \x01(\x08\"\xa2\x01\n\nUpdateItem\x12\x0f\n\x07type_id\x18\x01 \x01(\r\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\x12\x42\n\x08json_idx\x18\x03 \x03(\x0b\x32\x30.item_configurator_proto.UpdateItem.JsonIdxEntry\x1a.\n\x0cJsonIdxEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\"6\n\tUpdateRep\x12\x15\n\rrefresh_token\x18\x01 \x01(\t\x12\x12\n\nauthorized\x18\x02 \x01(\x08\"r\n\tUpdateReq\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rrefresh_token\x18\x02 \x01(\t\x12\x32\n\x05items\x18\x03 \x03(\x0b\x32#.item_configurator_proto.UpdateItem\x12\x0c\n\x04json\x18\x04 \x03(\t\"R\n\x11ListCharactersRep\x12\x12\n\ncharacters\x18\x01 \x03(\t\x12\x15\n\rrefresh_token\x18\x02 \x01(\t\x12\x12\n\nauthorized\x18\x03 \x01(\x08\"\xa6\x01\n\x11ListCharactersReq\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x34\n\tauth_kind\x18\x02 \x01(\x0e\x32!.item_configurator_proto.AuthKind\x12\x36\n\nauth_scope\x18\x03 \x01(\x0e\x32\".item_configurator_proto.AuthScope\x12\x15\n\rrefresh_token\x18\x04 \x01(\t\"=\n\x10\x41\x64\x64\x43haractersRep\x12\x15\n\rrefresh_token\x18\x01 \x01(\t\x12\x12\n\nauthorized\x18\x02 \x01(\x08\"\xb9\x01\n\x10\x41\x64\x64\x43haractersReq\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x34\n\tauth_kind\x18\x02 \x01(\x0e\x32!.item_configurator_proto.AuthKind\x12\x36\n\nauth_scope\x18\x03 \x01(\x0e\x32\".item_configurator_proto.AuthScope\x12\x15\n\rrefresh_token\x18\x04 \x01(\t\x12\x12\n\ncharacters\x18\x05 \x03(\t\"=\n\x10\x44\x65lCharactersRep\x12\x15\n\rrefresh_token\x18\x01 \x01(\t\x12\x12\n\nauthorized\x18\x02 \x01(\x08\"\xb9\x01\n\x10\x44\x65lCharactersReq\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x34\n\tauth_kind\x18\x02 \x01(\x0e\x32!.item_configurator_proto.AuthKind\x12\x36\n\nauth_scope\x18\x03 \x01(\x0e\x32\".item_configurator_proto.AuthScope\x12\x15\n\rrefresh_token\x18\x04 \x01(\t\x12\x12\n\ncharacters\x18\x05 \x03(\t\"\xb2\x01\n\x0f\x42uybackContract\x12\x36\n\x0c\x65si_contract\x18\x01 \x01(\x0b\x32 .weve_esi_proto.ExchangeContract\x12*\n\x0e\x63heck_contract\x18\x02 \x01(\x0b\x32\x12.buyback_proto.Rep\x12(\n\x0c\x62uy_contract\x18\x03 \x01(\x0b\x32\x12.buyback_proto.Rep\x12\x11\n\thash_code\x18\x04 \x01(\t\"\x81\x01\n\x13\x42uybackContractsReq\x12\x15\n\rinclude_items\x18\x01 \x01(\x08\x12\x15\n\rinclude_check\x18\x02 \x01(\x08\x12\x13\n\x0binclude_buy\x18\x03 \x01(\x08\x12\x15\n\rrefresh_token\x18\x04 \x01(\t\x12\x10\n\x08language\x18\x05 \x01(\t\"}\n\x13\x42uybackContractsRep\x12;\n\tcontracts\x18\x01 \x03(\x0b\x32(.item_configurator_proto.BuybackContract\x12\x15\n\rrefresh_token\x18\x02 \x01(\t\x12\x12\n\nauthorized\x18\x03 \x01(\x08*&\n\x05Query\x12\x08\n\x04TRUE\x10\x00\x12\t\n\x05\x46\x41LSE\x10\x01\x12\x08\n\x04\x42OTH\x10\x02*\x1f\n\x08\x41uthKind\x12\x08\n\x04READ\x10\x00\x12\t\n\x05WRITE\x10\x01*5\n\tAuthScope\x12\t\n\x05ITEMS\x10\x00\x12\x0e\n\nCHARACTERS\x10\x01\x12\r\n\tCONTRACTS\x10\x02\x32\xd8\x04\n\x10ItemConfigurator\x12P\n\x06Update\x12\".item_configurator_proto.UpdateReq\x1a\".item_configurator_proto.UpdateRep\x12J\n\x04List\x12 .item_configurator_proto.ListReq\x1a .item_configurator_proto.ListRep\x12h\n\x0eListCharacters\x12*.item_configurator_proto.ListCharactersReq\x1a*.item_configurator_proto.ListCharactersRep\x12\x65\n\rAddCharacters\x12).item_configurator_proto.AddCharactersReq\x1a).item_configurator_proto.AddCharactersRep\x12\x65\n\rDelCharacters\x12).item_configurator_proto.DelCharactersReq\x1a).item_configurator_proto.DelCharactersRep\x12n\n\x10\x42uybackContracts\x12,.item_configurator_proto.BuybackContractsReq\x1a,.item_configurator_proto.BuybackContractsRepb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'item_configurator_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LISTITEM_JSONIDXENTRY._options = None
  _LISTITEM_JSONIDXENTRY._serialized_options = b'8\001'
  _UPDATEITEM_JSONIDXENTRY._options = None
  _UPDATEITEM_JSONIDXENTRY._serialized_options = b'8\001'
  _QUERY._serialized_start=2342
  _QUERY._serialized_end=2380
  _AUTHKIND._serialized_start=2382
  _AUTHKIND._serialized_end=2413
  _AUTHSCOPE._serialized_start=2415
  _AUTHSCOPE._serialized_end=2468
  _LISTITEM._serialized_start=84
  _LISTITEM._serialized_end=323
  _LISTITEM_JSONIDXENTRY._serialized_start=277
  _LISTITEM_JSONIDXENTRY._serialized_end=323
  _LISTREP._serialized_start=326
  _LISTREP._serialized_end=501
  _LISTREQ._serialized_start=504
  _LISTREQ._serialized_end=808
  _UPDATEITEM._serialized_start=811
  _UPDATEITEM._serialized_end=973
  _UPDATEITEM_JSONIDXENTRY._serialized_start=277
  _UPDATEITEM_JSONIDXENTRY._serialized_end=323
  _UPDATEREP._serialized_start=975
  _UPDATEREP._serialized_end=1029
  _UPDATEREQ._serialized_start=1031
  _UPDATEREQ._serialized_end=1145
  _LISTCHARACTERSREP._serialized_start=1147
  _LISTCHARACTERSREP._serialized_end=1229
  _LISTCHARACTERSREQ._serialized_start=1232
  _LISTCHARACTERSREQ._serialized_end=1398
  _ADDCHARACTERSREP._serialized_start=1400
  _ADDCHARACTERSREP._serialized_end=1461
  _ADDCHARACTERSREQ._serialized_start=1464
  _ADDCHARACTERSREQ._serialized_end=1649
  _DELCHARACTERSREP._serialized_start=1651
  _DELCHARACTERSREP._serialized_end=1712
  _DELCHARACTERSREQ._serialized_start=1715
  _DELCHARACTERSREQ._serialized_end=1900
  _BUYBACKCONTRACT._serialized_start=1903
  _BUYBACKCONTRACT._serialized_end=2081
  _BUYBACKCONTRACTSREQ._serialized_start=2084
  _BUYBACKCONTRACTSREQ._serialized_end=2213
  _BUYBACKCONTRACTSREP._serialized_start=2215
  _BUYBACKCONTRACTSREP._serialized_end=2340
  _ITEMCONFIGURATOR._serialized_start=2471
  _ITEMCONFIGURATOR._serialized_end=3071
# @@protoc_insertion_point(module_scope)
