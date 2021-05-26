# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from mir_msgs/PowerBoardMotorStatus.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class PowerBoardMotorStatus(genpy.Message):
  _md5sum = "6fa84650aa5369a4240fff080dbf7c68"
  _type = "mir_msgs/PowerBoardMotorStatus"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """uint16 LeftMotor_CtrlWord
int32 LeftMotor_Speed
int32 LeftMotor_Encoder
uint16 LeftMotor_Status
uint8 LeftMotor_Error
uint32 LeftMotor_ErrorHist1
uint32 LeftMotor_ErrorHist2
int32 LeftMotor_Current
uint16 LeftMotor_I2t_Motor
uint16 LeftMotor_I2t_Controller
int16 LeftMotor_Temperature
uint16 RightMotor_CtrlWord
int32 RightMotor_Speed
int32 RightMotor_Encoder
uint16 RightMotor_Status
uint8 RightMotor_Error
uint32 RightMotor_ErrorHist1
uint32 RightMotor_ErrorHist2
int32 RightMotor_Current
uint16 RightMotor_I2t_Motor
uint16 RightMotor_I2t_Controller
int16 RightMotor_Temperature
uint8 Brake_LeftStatus
uint8 Brake_RightStatus"""
  __slots__ = ['LeftMotor_CtrlWord','LeftMotor_Speed','LeftMotor_Encoder','LeftMotor_Status','LeftMotor_Error','LeftMotor_ErrorHist1','LeftMotor_ErrorHist2','LeftMotor_Current','LeftMotor_I2t_Motor','LeftMotor_I2t_Controller','LeftMotor_Temperature','RightMotor_CtrlWord','RightMotor_Speed','RightMotor_Encoder','RightMotor_Status','RightMotor_Error','RightMotor_ErrorHist1','RightMotor_ErrorHist2','RightMotor_Current','RightMotor_I2t_Motor','RightMotor_I2t_Controller','RightMotor_Temperature','Brake_LeftStatus','Brake_RightStatus']
  _slot_types = ['uint16','int32','int32','uint16','uint8','uint32','uint32','int32','uint16','uint16','int16','uint16','int32','int32','uint16','uint8','uint32','uint32','int32','uint16','uint16','int16','uint8','uint8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       LeftMotor_CtrlWord,LeftMotor_Speed,LeftMotor_Encoder,LeftMotor_Status,LeftMotor_Error,LeftMotor_ErrorHist1,LeftMotor_ErrorHist2,LeftMotor_Current,LeftMotor_I2t_Motor,LeftMotor_I2t_Controller,LeftMotor_Temperature,RightMotor_CtrlWord,RightMotor_Speed,RightMotor_Encoder,RightMotor_Status,RightMotor_Error,RightMotor_ErrorHist1,RightMotor_ErrorHist2,RightMotor_Current,RightMotor_I2t_Motor,RightMotor_I2t_Controller,RightMotor_Temperature,Brake_LeftStatus,Brake_RightStatus

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(PowerBoardMotorStatus, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.LeftMotor_CtrlWord is None:
        self.LeftMotor_CtrlWord = 0
      if self.LeftMotor_Speed is None:
        self.LeftMotor_Speed = 0
      if self.LeftMotor_Encoder is None:
        self.LeftMotor_Encoder = 0
      if self.LeftMotor_Status is None:
        self.LeftMotor_Status = 0
      if self.LeftMotor_Error is None:
        self.LeftMotor_Error = 0
      if self.LeftMotor_ErrorHist1 is None:
        self.LeftMotor_ErrorHist1 = 0
      if self.LeftMotor_ErrorHist2 is None:
        self.LeftMotor_ErrorHist2 = 0
      if self.LeftMotor_Current is None:
        self.LeftMotor_Current = 0
      if self.LeftMotor_I2t_Motor is None:
        self.LeftMotor_I2t_Motor = 0
      if self.LeftMotor_I2t_Controller is None:
        self.LeftMotor_I2t_Controller = 0
      if self.LeftMotor_Temperature is None:
        self.LeftMotor_Temperature = 0
      if self.RightMotor_CtrlWord is None:
        self.RightMotor_CtrlWord = 0
      if self.RightMotor_Speed is None:
        self.RightMotor_Speed = 0
      if self.RightMotor_Encoder is None:
        self.RightMotor_Encoder = 0
      if self.RightMotor_Status is None:
        self.RightMotor_Status = 0
      if self.RightMotor_Error is None:
        self.RightMotor_Error = 0
      if self.RightMotor_ErrorHist1 is None:
        self.RightMotor_ErrorHist1 = 0
      if self.RightMotor_ErrorHist2 is None:
        self.RightMotor_ErrorHist2 = 0
      if self.RightMotor_Current is None:
        self.RightMotor_Current = 0
      if self.RightMotor_I2t_Motor is None:
        self.RightMotor_I2t_Motor = 0
      if self.RightMotor_I2t_Controller is None:
        self.RightMotor_I2t_Controller = 0
      if self.RightMotor_Temperature is None:
        self.RightMotor_Temperature = 0
      if self.Brake_LeftStatus is None:
        self.Brake_LeftStatus = 0
      if self.Brake_RightStatus is None:
        self.Brake_RightStatus = 0
    else:
      self.LeftMotor_CtrlWord = 0
      self.LeftMotor_Speed = 0
      self.LeftMotor_Encoder = 0
      self.LeftMotor_Status = 0
      self.LeftMotor_Error = 0
      self.LeftMotor_ErrorHist1 = 0
      self.LeftMotor_ErrorHist2 = 0
      self.LeftMotor_Current = 0
      self.LeftMotor_I2t_Motor = 0
      self.LeftMotor_I2t_Controller = 0
      self.LeftMotor_Temperature = 0
      self.RightMotor_CtrlWord = 0
      self.RightMotor_Speed = 0
      self.RightMotor_Encoder = 0
      self.RightMotor_Status = 0
      self.RightMotor_Error = 0
      self.RightMotor_ErrorHist1 = 0
      self.RightMotor_ErrorHist2 = 0
      self.RightMotor_Current = 0
      self.RightMotor_I2t_Motor = 0
      self.RightMotor_I2t_Controller = 0
      self.RightMotor_Temperature = 0
      self.Brake_LeftStatus = 0
      self.Brake_RightStatus = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_H2iHB2Ii2HhH2iHB2Ii2Hh2B().pack(_x.LeftMotor_CtrlWord, _x.LeftMotor_Speed, _x.LeftMotor_Encoder, _x.LeftMotor_Status, _x.LeftMotor_Error, _x.LeftMotor_ErrorHist1, _x.LeftMotor_ErrorHist2, _x.LeftMotor_Current, _x.LeftMotor_I2t_Motor, _x.LeftMotor_I2t_Controller, _x.LeftMotor_Temperature, _x.RightMotor_CtrlWord, _x.RightMotor_Speed, _x.RightMotor_Encoder, _x.RightMotor_Status, _x.RightMotor_Error, _x.RightMotor_ErrorHist1, _x.RightMotor_ErrorHist2, _x.RightMotor_Current, _x.RightMotor_I2t_Motor, _x.RightMotor_I2t_Controller, _x.RightMotor_Temperature, _x.Brake_LeftStatus, _x.Brake_RightStatus))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 64
      (_x.LeftMotor_CtrlWord, _x.LeftMotor_Speed, _x.LeftMotor_Encoder, _x.LeftMotor_Status, _x.LeftMotor_Error, _x.LeftMotor_ErrorHist1, _x.LeftMotor_ErrorHist2, _x.LeftMotor_Current, _x.LeftMotor_I2t_Motor, _x.LeftMotor_I2t_Controller, _x.LeftMotor_Temperature, _x.RightMotor_CtrlWord, _x.RightMotor_Speed, _x.RightMotor_Encoder, _x.RightMotor_Status, _x.RightMotor_Error, _x.RightMotor_ErrorHist1, _x.RightMotor_ErrorHist2, _x.RightMotor_Current, _x.RightMotor_I2t_Motor, _x.RightMotor_I2t_Controller, _x.RightMotor_Temperature, _x.Brake_LeftStatus, _x.Brake_RightStatus,) = _get_struct_H2iHB2Ii2HhH2iHB2Ii2Hh2B().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_H2iHB2Ii2HhH2iHB2Ii2Hh2B().pack(_x.LeftMotor_CtrlWord, _x.LeftMotor_Speed, _x.LeftMotor_Encoder, _x.LeftMotor_Status, _x.LeftMotor_Error, _x.LeftMotor_ErrorHist1, _x.LeftMotor_ErrorHist2, _x.LeftMotor_Current, _x.LeftMotor_I2t_Motor, _x.LeftMotor_I2t_Controller, _x.LeftMotor_Temperature, _x.RightMotor_CtrlWord, _x.RightMotor_Speed, _x.RightMotor_Encoder, _x.RightMotor_Status, _x.RightMotor_Error, _x.RightMotor_ErrorHist1, _x.RightMotor_ErrorHist2, _x.RightMotor_Current, _x.RightMotor_I2t_Motor, _x.RightMotor_I2t_Controller, _x.RightMotor_Temperature, _x.Brake_LeftStatus, _x.Brake_RightStatus))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 64
      (_x.LeftMotor_CtrlWord, _x.LeftMotor_Speed, _x.LeftMotor_Encoder, _x.LeftMotor_Status, _x.LeftMotor_Error, _x.LeftMotor_ErrorHist1, _x.LeftMotor_ErrorHist2, _x.LeftMotor_Current, _x.LeftMotor_I2t_Motor, _x.LeftMotor_I2t_Controller, _x.LeftMotor_Temperature, _x.RightMotor_CtrlWord, _x.RightMotor_Speed, _x.RightMotor_Encoder, _x.RightMotor_Status, _x.RightMotor_Error, _x.RightMotor_ErrorHist1, _x.RightMotor_ErrorHist2, _x.RightMotor_Current, _x.RightMotor_I2t_Motor, _x.RightMotor_I2t_Controller, _x.RightMotor_Temperature, _x.Brake_LeftStatus, _x.Brake_RightStatus,) = _get_struct_H2iHB2Ii2HhH2iHB2Ii2Hh2B().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_H2iHB2Ii2HhH2iHB2Ii2Hh2B = None
def _get_struct_H2iHB2Ii2HhH2iHB2Ii2Hh2B():
    global _struct_H2iHB2Ii2HhH2iHB2Ii2Hh2B
    if _struct_H2iHB2Ii2HhH2iHB2Ii2Hh2B is None:
        _struct_H2iHB2Ii2HhH2iHB2Ii2Hh2B = struct.Struct("<H2iHB2Ii2HhH2iHB2Ii2Hh2B")
    return _struct_H2iHB2Ii2HhH2iHB2Ii2Hh2B
