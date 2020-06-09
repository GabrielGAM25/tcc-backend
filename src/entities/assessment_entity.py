class AssessmentEntity():
    def __init__(
            self,
            id_,
            user_id,
            date,
            weight,
            fat_percentage,
            neck,
            shoulder,
            torax,
            abdomen,
            waist,
            hip,
            left_arm,
            right_arm,
            left_forearm,
            right_forearm,
            left_thigh,
            right_thigh,
            left_calf,
            right_calf,
    ):
        self.id = id_
        self.user_id = user_id
        self.date = date
        self.weight = weight
        self.fat_percentage = fat_percentage
        self.neck = neck
        self.shoulder = shoulder
        self.torax = torax
        self.abdomen = abdomen
        self.waist = waist
        self.hip = hip
        self.left_arm = left_arm
        self.right_arm = right_arm
        self.left_forearm = left_forearm
        self.right_forearm = right_forearm
        self.left_thigh = left_thigh
        self.right_thigh = right_thigh
        self.left_calf = left_calf
        self.right_calf = right_calf

    def __repr__(self):
        return f'<Assessment id:{self.id} user_id:{self.user_id} date:{self.date}>'

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'date': self.date,
            'weight': float(self.weight),
            'fat_percentage': float(self.fat_percentage),
            'neck': float(self.neck),
            'shoulder': float(self.shoulder),
            'torax': float(self.torax),
            'abdomen': float(self.abdomen),
            'waist': float(self.waist),
            'hip': float(self.hip),
            'left_arm': float(self.left_arm),
            'right_arm': float(self.right_arm),
            'left_forearm': float(self.left_forearm),
            'right_forearm': float(self.right_forearm),
            'left_thigh': float(self.left_thigh),
            'right_thigh': float(self.right_thigh),
            'left_calf': float(self.left_calf),
            'right_calf': float(self.right_calf),
        }
