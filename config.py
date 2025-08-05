D_DTYPE = {
    'รหัสทรัพย์สิน': str,
    'ประเภทอสังหาฯ': str,
    'หมู่บ้าน/คอนโด': str,
    'datasource': str,
    'confidence_type': str,
    'ราคาประเมินที่ กค รับรอง': float,
    'count': float,
    'avg': float,
    'max': float,
    'min': float,
    'closest': str
}

D_RENAME = {
    'รหัสทรัพย์สิน': 'asset_id',
    'ประเภทอสังหาฯ': 'pty_tp',
    'หมู่บ้าน/คอนโด': 'hs_nm',
    'datasource': 'datasource',
    'confidence_type': 'confidence_type',
    'ราคาประเมินที่ กค รับรอง': 'aprs_prc',
    'count': 'count',
    'avg': 'avg_prc',
    'max': 'max_prc',
    'min': 'min_prc',
    'closest': 'closest'
}