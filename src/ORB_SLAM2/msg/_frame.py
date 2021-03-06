# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ORB_SLAM2/frame.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import ORB_SLAM2.msg
import std_msgs.msg

class frame(genpy.Message):
  _md5sum = "083ce032fac5ff267ed4fa143763b28a"
  _type = "ORB_SLAM2/frame"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """Header header

#this is the msg for Frame info

#for Sharing Map
int32 mnMachineId

#Frame timestamp.
float64 mTimeStamp

#Number of KeyPoints.
int32 N

## Vector of keypoints (original for visualization) and undistorted (actually used by the system).
## In the stereo case, mvKeysUn is redundant as images must be rectified.
## In the RGB-D case, RGB images can be distorted.
#std::vector<cv::KeyPoint> mvKeys, mvKeysRight
keypoint[] mvKeysUn

## Corresponding stereo coordinate and depth for each keypoint.
## "Monocular" keypoints have a negative value.
#floatVector mvuRight
#std::vector<float> mvDepth

# Bag of Words Vector structures.
bow[] mBowVec
feature[] mFeatVec

# ORB descriptor, each row associated to a keypoint.
descriptor[] mDescriptors

## MapPoints associated to keypoints, NULL pointer if no association.
#std::vector<MapPoint*> mvpMapPoints
# Flag to identify outlier associations.
bool[] mvbOutlier

# Camera pose.
float32Vector[] mTcw

# Current and Next Frame id.
int32 nNextId
int32 mnId

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: ORB_SLAM2/keypoint
int32 x
int32 y
float32 angle
int32 class_id
int32 octave
float32 response
float32 size

================================================================================
MSG: ORB_SLAM2/bow
uint32   WordId
float64  WordValue

================================================================================
MSG: ORB_SLAM2/feature
uint32 NodeId
uint32[]  i_feature

================================================================================
MSG: ORB_SLAM2/descriptor
uint8[] descriptor

================================================================================
MSG: ORB_SLAM2/float32Vector
float32[] float32Vector
"""
  __slots__ = ['header','mnMachineId','mTimeStamp','N','mvKeysUn','mBowVec','mFeatVec','mDescriptors','mvbOutlier','mTcw','nNextId','mnId']
  _slot_types = ['std_msgs/Header','int32','float64','int32','ORB_SLAM2/keypoint[]','ORB_SLAM2/bow[]','ORB_SLAM2/feature[]','ORB_SLAM2/descriptor[]','bool[]','ORB_SLAM2/float32Vector[]','int32','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,mnMachineId,mTimeStamp,N,mvKeysUn,mBowVec,mFeatVec,mDescriptors,mvbOutlier,mTcw,nNextId,mnId

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(frame, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.mnMachineId is None:
        self.mnMachineId = 0
      if self.mTimeStamp is None:
        self.mTimeStamp = 0.
      if self.N is None:
        self.N = 0
      if self.mvKeysUn is None:
        self.mvKeysUn = []
      if self.mBowVec is None:
        self.mBowVec = []
      if self.mFeatVec is None:
        self.mFeatVec = []
      if self.mDescriptors is None:
        self.mDescriptors = []
      if self.mvbOutlier is None:
        self.mvbOutlier = []
      if self.mTcw is None:
        self.mTcw = []
      if self.nNextId is None:
        self.nNextId = 0
      if self.mnId is None:
        self.mnId = 0
    else:
      self.header = std_msgs.msg.Header()
      self.mnMachineId = 0
      self.mTimeStamp = 0.
      self.N = 0
      self.mvKeysUn = []
      self.mBowVec = []
      self.mFeatVec = []
      self.mDescriptors = []
      self.mvbOutlier = []
      self.mTcw = []
      self.nNextId = 0
      self.mnId = 0

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
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_idi().pack(_x.mnMachineId, _x.mTimeStamp, _x.N))
      length = len(self.mvKeysUn)
      buff.write(_struct_I.pack(length))
      for val1 in self.mvKeysUn:
        _x = val1
        buff.write(_get_struct_2if2i2f().pack(_x.x, _x.y, _x.angle, _x.class_id, _x.octave, _x.response, _x.size))
      length = len(self.mBowVec)
      buff.write(_struct_I.pack(length))
      for val1 in self.mBowVec:
        _x = val1
        buff.write(_get_struct_Id().pack(_x.WordId, _x.WordValue))
      length = len(self.mFeatVec)
      buff.write(_struct_I.pack(length))
      for val1 in self.mFeatVec:
        buff.write(_get_struct_I().pack(val1.NodeId))
        length = len(val1.i_feature)
        buff.write(_struct_I.pack(length))
        pattern = '<%sI'%length
        buff.write(struct.pack(pattern, *val1.i_feature))
      length = len(self.mDescriptors)
      buff.write(_struct_I.pack(length))
      for val1 in self.mDescriptors:
        _x = val1.descriptor
        length = len(_x)
        # - if encoded as a list instead, serialize as bytes instead of string
        if type(_x) in [list, tuple]:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.mvbOutlier)
      buff.write(_struct_I.pack(length))
      pattern = '<%sB'%length
      buff.write(struct.pack(pattern, *self.mvbOutlier))
      length = len(self.mTcw)
      buff.write(_struct_I.pack(length))
      for val1 in self.mTcw:
        length = len(val1.float32Vector)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(struct.pack(pattern, *val1.float32Vector))
      _x = self
      buff.write(_get_struct_2i().pack(_x.nNextId, _x.mnId))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.mvKeysUn is None:
        self.mvKeysUn = None
      if self.mBowVec is None:
        self.mBowVec = None
      if self.mFeatVec is None:
        self.mFeatVec = None
      if self.mDescriptors is None:
        self.mDescriptors = None
      if self.mTcw is None:
        self.mTcw = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.mnMachineId, _x.mTimeStamp, _x.N,) = _get_struct_idi().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.mvKeysUn = []
      for i in range(0, length):
        val1 = ORB_SLAM2.msg.keypoint()
        _x = val1
        start = end
        end += 28
        (_x.x, _x.y, _x.angle, _x.class_id, _x.octave, _x.response, _x.size,) = _get_struct_2if2i2f().unpack(str[start:end])
        self.mvKeysUn.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.mBowVec = []
      for i in range(0, length):
        val1 = ORB_SLAM2.msg.bow()
        _x = val1
        start = end
        end += 12
        (_x.WordId, _x.WordValue,) = _get_struct_Id().unpack(str[start:end])
        self.mBowVec.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.mFeatVec = []
      for i in range(0, length):
        val1 = ORB_SLAM2.msg.feature()
        start = end
        end += 4
        (val1.NodeId,) = _get_struct_I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sI'%length
        start = end
        end += struct.calcsize(pattern)
        val1.i_feature = struct.unpack(pattern, str[start:end])
        self.mFeatVec.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.mDescriptors = []
      for i in range(0, length):
        val1 = ORB_SLAM2.msg.descriptor()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        val1.descriptor = str[start:end]
        self.mDescriptors.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sB'%length
      start = end
      end += struct.calcsize(pattern)
      self.mvbOutlier = struct.unpack(pattern, str[start:end])
      self.mvbOutlier = map(bool, self.mvbOutlier)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.mTcw = []
      for i in range(0, length):
        val1 = ORB_SLAM2.msg.float32Vector()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        end += struct.calcsize(pattern)
        val1.float32Vector = struct.unpack(pattern, str[start:end])
        self.mTcw.append(val1)
      _x = self
      start = end
      end += 8
      (_x.nNextId, _x.mnId,) = _get_struct_2i().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_idi().pack(_x.mnMachineId, _x.mTimeStamp, _x.N))
      length = len(self.mvKeysUn)
      buff.write(_struct_I.pack(length))
      for val1 in self.mvKeysUn:
        _x = val1
        buff.write(_get_struct_2if2i2f().pack(_x.x, _x.y, _x.angle, _x.class_id, _x.octave, _x.response, _x.size))
      length = len(self.mBowVec)
      buff.write(_struct_I.pack(length))
      for val1 in self.mBowVec:
        _x = val1
        buff.write(_get_struct_Id().pack(_x.WordId, _x.WordValue))
      length = len(self.mFeatVec)
      buff.write(_struct_I.pack(length))
      for val1 in self.mFeatVec:
        buff.write(_get_struct_I().pack(val1.NodeId))
        length = len(val1.i_feature)
        buff.write(_struct_I.pack(length))
        pattern = '<%sI'%length
        buff.write(val1.i_feature.tostring())
      length = len(self.mDescriptors)
      buff.write(_struct_I.pack(length))
      for val1 in self.mDescriptors:
        _x = val1.descriptor
        length = len(_x)
        # - if encoded as a list instead, serialize as bytes instead of string
        if type(_x) in [list, tuple]:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.mvbOutlier)
      buff.write(_struct_I.pack(length))
      pattern = '<%sB'%length
      buff.write(self.mvbOutlier.tostring())
      length = len(self.mTcw)
      buff.write(_struct_I.pack(length))
      for val1 in self.mTcw:
        length = len(val1.float32Vector)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(val1.float32Vector.tostring())
      _x = self
      buff.write(_get_struct_2i().pack(_x.nNextId, _x.mnId))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.mvKeysUn is None:
        self.mvKeysUn = None
      if self.mBowVec is None:
        self.mBowVec = None
      if self.mFeatVec is None:
        self.mFeatVec = None
      if self.mDescriptors is None:
        self.mDescriptors = None
      if self.mTcw is None:
        self.mTcw = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.mnMachineId, _x.mTimeStamp, _x.N,) = _get_struct_idi().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.mvKeysUn = []
      for i in range(0, length):
        val1 = ORB_SLAM2.msg.keypoint()
        _x = val1
        start = end
        end += 28
        (_x.x, _x.y, _x.angle, _x.class_id, _x.octave, _x.response, _x.size,) = _get_struct_2if2i2f().unpack(str[start:end])
        self.mvKeysUn.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.mBowVec = []
      for i in range(0, length):
        val1 = ORB_SLAM2.msg.bow()
        _x = val1
        start = end
        end += 12
        (_x.WordId, _x.WordValue,) = _get_struct_Id().unpack(str[start:end])
        self.mBowVec.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.mFeatVec = []
      for i in range(0, length):
        val1 = ORB_SLAM2.msg.feature()
        start = end
        end += 4
        (val1.NodeId,) = _get_struct_I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sI'%length
        start = end
        end += struct.calcsize(pattern)
        val1.i_feature = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=length)
        self.mFeatVec.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.mDescriptors = []
      for i in range(0, length):
        val1 = ORB_SLAM2.msg.descriptor()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        val1.descriptor = str[start:end]
        self.mDescriptors.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sB'%length
      start = end
      end += struct.calcsize(pattern)
      self.mvbOutlier = numpy.frombuffer(str[start:end], dtype=numpy.bool, count=length)
      self.mvbOutlier = map(bool, self.mvbOutlier)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.mTcw = []
      for i in range(0, length):
        val1 = ORB_SLAM2.msg.float32Vector()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        end += struct.calcsize(pattern)
        val1.float32Vector = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
        self.mTcw.append(val1)
      _x = self
      start = end
      end += 8
      (_x.nNextId, _x.mnId,) = _get_struct_2i().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_idi = None
def _get_struct_idi():
    global _struct_idi
    if _struct_idi is None:
        _struct_idi = struct.Struct("<idi")
    return _struct_idi
_struct_Id = None
def _get_struct_Id():
    global _struct_Id
    if _struct_Id is None:
        _struct_Id = struct.Struct("<Id")
    return _struct_Id
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_2if2i2f = None
def _get_struct_2if2i2f():
    global _struct_2if2i2f
    if _struct_2if2i2f is None:
        _struct_2if2i2f = struct.Struct("<2if2i2f")
    return _struct_2if2i2f
_struct_2i = None
def _get_struct_2i():
    global _struct_2i
    if _struct_2i is None:
        _struct_2i = struct.Struct("<2i")
    return _struct_2i
