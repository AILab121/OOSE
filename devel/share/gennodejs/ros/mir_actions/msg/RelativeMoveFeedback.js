// Auto-generated. Do not edit!

// (in-package mir_actions.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------

class RelativeMoveFeedback {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.state = null;
      this.current_goal = null;
      this.dist_to_goal = null;
    }
    else {
      if (initObj.hasOwnProperty('state')) {
        this.state = initObj.state
      }
      else {
        this.state = 0;
      }
      if (initObj.hasOwnProperty('current_goal')) {
        this.current_goal = initObj.current_goal
      }
      else {
        this.current_goal = new geometry_msgs.msg.PoseStamped();
      }
      if (initObj.hasOwnProperty('dist_to_goal')) {
        this.dist_to_goal = initObj.dist_to_goal
      }
      else {
        this.dist_to_goal = new geometry_msgs.msg.PoseStamped();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type RelativeMoveFeedback
    // Serialize message field [state]
    bufferOffset = _serializer.int8(obj.state, buffer, bufferOffset);
    // Serialize message field [current_goal]
    bufferOffset = geometry_msgs.msg.PoseStamped.serialize(obj.current_goal, buffer, bufferOffset);
    // Serialize message field [dist_to_goal]
    bufferOffset = geometry_msgs.msg.PoseStamped.serialize(obj.dist_to_goal, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type RelativeMoveFeedback
    let len;
    let data = new RelativeMoveFeedback(null);
    // Deserialize message field [state]
    data.state = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [current_goal]
    data.current_goal = geometry_msgs.msg.PoseStamped.deserialize(buffer, bufferOffset);
    // Deserialize message field [dist_to_goal]
    data.dist_to_goal = geometry_msgs.msg.PoseStamped.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += geometry_msgs.msg.PoseStamped.getMessageSize(object.current_goal);
    length += geometry_msgs.msg.PoseStamped.getMessageSize(object.dist_to_goal);
    return length + 1;
  }

  static datatype() {
    // Returns string type for a message object
    return 'mir_actions/RelativeMoveFeedback';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '95b697bacf828ff88c46362efe2f6b7e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
    #feedback
    int8 DOCKING = 0
    int8 COLLISION = 1
    int8 state
    geometry_msgs/PoseStamped current_goal
    geometry_msgs/PoseStamped dist_to_goal
    
    
    ================================================================================
    MSG: geometry_msgs/PoseStamped
    # A Pose with reference coordinate frame and timestamp
    Header header
    Pose pose
    
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
    string frame_id
    
    ================================================================================
    MSG: geometry_msgs/Pose
    # A representation of pose in free space, composed of position and orientation. 
    Point position
    Quaternion orientation
    
    ================================================================================
    MSG: geometry_msgs/Point
    # This contains the position of a point in free space
    float64 x
    float64 y
    float64 z
    
    ================================================================================
    MSG: geometry_msgs/Quaternion
    # This represents an orientation in free space in quaternion form.
    
    float64 x
    float64 y
    float64 z
    float64 w
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new RelativeMoveFeedback(null);
    if (msg.state !== undefined) {
      resolved.state = msg.state;
    }
    else {
      resolved.state = 0
    }

    if (msg.current_goal !== undefined) {
      resolved.current_goal = geometry_msgs.msg.PoseStamped.Resolve(msg.current_goal)
    }
    else {
      resolved.current_goal = new geometry_msgs.msg.PoseStamped()
    }

    if (msg.dist_to_goal !== undefined) {
      resolved.dist_to_goal = geometry_msgs.msg.PoseStamped.Resolve(msg.dist_to_goal)
    }
    else {
      resolved.dist_to_goal = new geometry_msgs.msg.PoseStamped()
    }

    return resolved;
    }
};

// Constants for message
RelativeMoveFeedback.Constants = {
  DOCKING: 0,
  COLLISION: 1,
}

module.exports = RelativeMoveFeedback;
