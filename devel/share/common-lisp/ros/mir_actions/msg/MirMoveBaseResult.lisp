; Auto-generated. Do not edit!


(cl:in-package mir_actions-msg)


;//! \htmlinclude MirMoveBaseResult.msg.html

(cl:defclass <MirMoveBaseResult> (roslisp-msg-protocol:ros-message)
  ((end_state
    :reader end_state
    :initarg :end_state
    :type cl:fixnum
    :initform 0)
   (end_pose
    :reader end_pose
    :initarg :end_pose
    :type geometry_msgs-msg:PoseStamped
    :initform (cl:make-instance 'geometry_msgs-msg:PoseStamped)))
)

(cl:defclass MirMoveBaseResult (<MirMoveBaseResult>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MirMoveBaseResult>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MirMoveBaseResult)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name mir_actions-msg:<MirMoveBaseResult> is deprecated: use mir_actions-msg:MirMoveBaseResult instead.")))

(cl:ensure-generic-function 'end_state-val :lambda-list '(m))
(cl:defmethod end_state-val ((m <MirMoveBaseResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mir_actions-msg:end_state-val is deprecated.  Use mir_actions-msg:end_state instead.")
  (end_state m))

(cl:ensure-generic-function 'end_pose-val :lambda-list '(m))
(cl:defmethod end_pose-val ((m <MirMoveBaseResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mir_actions-msg:end_pose-val is deprecated.  Use mir_actions-msg:end_pose instead.")
  (end_pose m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<MirMoveBaseResult>)))
    "Constants for message type '<MirMoveBaseResult>"
  '((:UNDEFINED . 0)
    (:GOAL_REACHED . 1)
    (:FAILED . -1)
    (:FAILED_NO_PATH . -2)
    (:FAILED_GOAL_IN_STATIC_OBSTACLE . -3)
    (:FAILED_GOAL_IN_FORBIDDEN_AREA . -4)
    (:FAILED_GOAL_IN_DYNAMIC_OBSTACLE . -5)
    (:FAILED_ROBOT_IN_COLLISION . -6)
    (:FAILED_ROBOT_IN_FORBIDDEN_AREA . -7)
    (:FAILED_UNKNOWN_TRAILER . -8))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'MirMoveBaseResult)))
    "Constants for message type 'MirMoveBaseResult"
  '((:UNDEFINED . 0)
    (:GOAL_REACHED . 1)
    (:FAILED . -1)
    (:FAILED_NO_PATH . -2)
    (:FAILED_GOAL_IN_STATIC_OBSTACLE . -3)
    (:FAILED_GOAL_IN_FORBIDDEN_AREA . -4)
    (:FAILED_GOAL_IN_DYNAMIC_OBSTACLE . -5)
    (:FAILED_ROBOT_IN_COLLISION . -6)
    (:FAILED_ROBOT_IN_FORBIDDEN_AREA . -7)
    (:FAILED_UNKNOWN_TRAILER . -8))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MirMoveBaseResult>) ostream)
  "Serializes a message object of type '<MirMoveBaseResult>"
  (cl:let* ((signed (cl:slot-value msg 'end_state)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'end_pose) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MirMoveBaseResult>) istream)
  "Deserializes a message object of type '<MirMoveBaseResult>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'end_state) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'end_pose) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MirMoveBaseResult>)))
  "Returns string type for a message object of type '<MirMoveBaseResult>"
  "mir_actions/MirMoveBaseResult")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MirMoveBaseResult)))
  "Returns string type for a message object of type 'MirMoveBaseResult"
  "mir_actions/MirMoveBaseResult")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MirMoveBaseResult>)))
  "Returns md5sum for a message object of type '<MirMoveBaseResult>"
  "5d78ef95801ef85ff0171f7a59e041d7")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MirMoveBaseResult)))
  "Returns md5sum for a message object of type 'MirMoveBaseResult"
  "5d78ef95801ef85ff0171f7a59e041d7")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MirMoveBaseResult>)))
  "Returns full string definition for message of type '<MirMoveBaseResult>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#result definition~%int16 UNDEFINED = 0~%int16 GOAL_REACHED = 1~%int16 FAILED = -1~%int16 FAILED_NO_PATH = -2~%int16 FAILED_GOAL_IN_STATIC_OBSTACLE = -3~%int16 FAILED_GOAL_IN_FORBIDDEN_AREA = -4~%int16 FAILED_GOAL_IN_DYNAMIC_OBSTACLE = -5~%int16 FAILED_ROBOT_IN_COLLISION = -6~%int16 FAILED_ROBOT_IN_FORBIDDEN_AREA = -7~%int16 FAILED_UNKNOWN_TRAILER = -8~%int16 end_state~%geometry_msgs/PoseStamped end_pose~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MirMoveBaseResult)))
  "Returns full string definition for message of type 'MirMoveBaseResult"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#result definition~%int16 UNDEFINED = 0~%int16 GOAL_REACHED = 1~%int16 FAILED = -1~%int16 FAILED_NO_PATH = -2~%int16 FAILED_GOAL_IN_STATIC_OBSTACLE = -3~%int16 FAILED_GOAL_IN_FORBIDDEN_AREA = -4~%int16 FAILED_GOAL_IN_DYNAMIC_OBSTACLE = -5~%int16 FAILED_ROBOT_IN_COLLISION = -6~%int16 FAILED_ROBOT_IN_FORBIDDEN_AREA = -7~%int16 FAILED_UNKNOWN_TRAILER = -8~%int16 end_state~%geometry_msgs/PoseStamped end_pose~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MirMoveBaseResult>))
  (cl:+ 0
     2
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'end_pose))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MirMoveBaseResult>))
  "Converts a ROS message object to a list"
  (cl:list 'MirMoveBaseResult
    (cl:cons ':end_state (end_state msg))
    (cl:cons ':end_pose (end_pose msg))
))
