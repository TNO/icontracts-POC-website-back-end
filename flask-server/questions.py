from typing import Any, Dict

def freelance(data: Dict[str, Any]) -> Dict[str,Any]:
    data['price']['label'] = 'What is your expected price for this project?'
    return data

def questions() -> Dict[str,Any]:
    price_options = ['500-1000','1000-1500','1500-2000','2000-2500','2500-3000']
    milestone_options = ['Information gathering', 'Draft design selection', '1st Draft delivery', '2nd Draft delivery', 'Final delivery']
    payment_schedule_options = ['Prepayment', 'Milestone payment', 'Final payment']
    payment_options = ['Cash', 'Bank transfer', 'Bitcoin']

    return {
        'price': {
            'name': 'price',
            'label': 'What is your budget for this project?',
            'type': 'radio',
            'rows': 1,
            'input_class':'single-row',
            'prefix': '€',
            'options': price_options,
            'options_freelancer': price_options,
            'showRiskModel': False,
            'askAdditionalQuestion': False,
            'legalConfirmed': False,
            'variables': '',
            'risks': '',
            'values': [],
            'additionalInfo': '',
        },
        'milestones': {
            'name': 'milestones',
            'label': 'What is your preferred milestone plan?',
            'type': 'checkbox',
            'rows': 3,
            'options': milestone_options,
            'options_freelancer': milestone_options,
            'showRiskModel': False,
            'askAdditionalQuestion': False,
            'legalConfirmed': False,
            'variables': '',
            'risks': '',
            'values': [],
            'additionalInfo': '',
        },
        'payment_schedule': {
            'name': 'payment_schedule',
            'label': 'What is your preferred payment schedule?',
            'type': 'radio',
            'rows': 3,
            'options': payment_schedule_options,
            'options_freelancer': payment_schedule_options,
            'showRiskModel': False,
            'askAdditionalQuestion': False,
            'legalConfirmed': False,
            'variables': '',
            'risks': '',
            'values': [],
            'additionalInfo': '',
        },
        'payment_method': {
            'name': 'payment_method',
            'label': 'What is your preferred payment method?',
            'type': 'radio',
            'rows': 1,
            'input_class': 'single-row',
            'options': payment_options,
            'options_freelancer': payment_options,
            'showRiskModel': False,
            'askAdditionalQuestion': False,
            'legalConfirmed': False,
            'variables': '',
            'risks': '',
            'values': [],
            'additionalInfo': '',
        },
    }

def survey_questions() -> Dict[str, str]:
    return {
        'Trustworthiness': {
            'privacy': {
                'label': 'How do you rate the level of privacy you experienced?',
                'definition': 'By privacy we mean the level of protection of the contractor\'s personal data in the negotiation process.'
            },
            'inclusion': {
                'label': 'How do you rate the level of inclusivity you experienced?',
                'definition': 'By inclusivity we mean the degree of which the contractor\'s perspective is taken sufficiently into consideration in the negotiation process.'
            },
            'safety': {
                'label': 'How do you rate the level of safety you experienced?',
                'definition': 'By safety we mean the contractor\'s feeling of security in the process of providing sensitive information regarding the contract and the negotiation.'
            },
            'fairness': {
                'label': 'How do you rate the level of fairness you experienced?',
                'definition': 'By fairness we mean the degree of equality between the contractors during the negotiation phase.'
            },
        },
        'Effectiveness': {
            'speed': {
                'label': 'How do you rate the level of speed you experienced?',
                'definition': 'By speed we mean the quickness a contractor is able to provide all information for the contract.'
            },
            'usability': {
                'label': 'How do you rate the level of usability you experienced?',
                'definition': 'By usability we mean the degree to which it is more easy for the contractor to adequately provide the necessary information for the contract.'
            },
            'precision': {
                'label': 'How do you rate the level of precision you experienced?',
                'definition': 'By precision we mean the degree to which the contractor is able to fully and accurately deliver the required information for the contract.'
            },
            'collaboration': {
                'label': 'How do you rate the level of feasibility you experienced?',
                'definition': 'By feasibility we mean the degree to which it is possible for the contractor to provide all the required information for the contract.'
            }
        }
    }