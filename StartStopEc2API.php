<?php







function callAPI($method, $url, $data){
    $curl = curl_init();
    switch ($method){
       case "POST":
          curl_setopt($curl, CURLOPT_POST, 1);
          if ($data)
             curl_setopt($curl, CURLOPT_POSTFIELDS, $data);
          break;
       case "PUT":
          curl_setopt($curl, CURLOPT_CUSTOMREQUEST, "PUT");
          if ($data)
             curl_setopt($curl, CURLOPT_POSTFIELDS, $data);
          break;
       default:
          if ($data)
             $url = sprintf("%s?%s", $url, http_build_query($data));
    }
    curl_setopt($curl, CURLOPT_URL, $url);
    curl_setopt($curl, CURLOPT_HTTPHEADER, array('APIKEY: 111111111111111111111', 'Content-Type: application/json'));
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($curl, CURLOPT_HTTPAUTH, CURLAUTH_BASIC);
    $result = curl_exec($curl);
    if(!$result){die("Connection Failure");}
    curl_close($curl);
    return $result;
}
function getMapUrl($MapName, $defaultTimezone){
    $MapLoginAPI = "https://tmpewem15g.execute-api.ap-south-1.amazonaws.com/production/map";
    $url = $MapLoginAPI."?MapName=".$MapName."&ID=".$current_user->ID."&user_login=".$current_user->user_login."&user_email=".$current_user->user_email."&user_firstname=".$current_user->user_firstname."&user_lastname=".$current_user->user_lastname."&display_name=".$current_user->display_name."&timezone=".$defaultTimezone;
    return $url;
}
// A send custom WebHook
add_action( 'elementor_pro/forms/new_record', function( $record, $handler ) {
    $current_user = wp_get_current_user();
    $defaultTimezone = date_default_timezone_get();
	$form_name = $record->get_form_settings( 'form_name' );

	if ( $form_name == 'start_instance') {
	    // parse out the gender value.
	    $raw_fields = $record->get( 'fields' );
        $fields = [];
        foreach ( $raw_fields as $id => $field ) {
            $fields[ $id ] = $field['value'];
        }
		if(!$current_user->exists()){   //(bool) True if user is logged in, false if not logged in.
			$output['message']="Message: You are not logged in. Login first.";
			$output['message_terminate']="Message:";
			$handler->add_response_data(true, $output);
		}else{
		    $StartStopEc2InstanceAPI = "https://fc6cd7kk63.execute-api.ap-south-1.amazonaws.com/Production/cc";
		    $url = $StartStopEc2InstanceAPI."?terminate=0&user_login=".$current_user->user_login."&user_email=".$current_user->user_email."&gender=".$fields["gender"]."&timezone=".$defaultTimezone;
            $response =  json_decode(callAPI('GET', $url, false), true);
			$output['message']="Public DNS Name: ".$response['public_dns_name'];
			$output['message_terminate']="Message:";
			$handler->add_response_data(true, $output);
		}
	}elseif( $form_name == 'terminate_instance') {
		if(!$current_user->exists()){
			$output['message']="Message:";
			$output['message_terminate']="Message: You are not logged in. Login first.";
			$handler->add_response_data(true, $output);
		}else{
		    $StartStopEc2InstanceAPI = "https://fc6cd7kk63.execute-api.ap-south-1.amazonaws.com/Production/cc";
		    $url = $StartStopEc2InstanceAPI."?terminate=1&user_login=".$current_user->user_login."&user_email=".$current_user->user_email."&timezone=".$defaultTimezone;
            $response = json_decode(callAPI('GET', $url, false), true);
			if($response['terminate'] == "1"){
				$output['message']="Public DNS Name: ".$response['public_dns_name'];
				$output['message_terminate']= "Message: Instance having public DNS name ".$response['public_dns_name']." termination successful.";
			}else{
				$output['message']="Public DNS Name: ";
				$output['message_terminate']= "Message: all your instances have already terminated.";
			}
			$handler->add_response_data(true, $output);
		}
	}elseif( $form_name == 'Map1') {
		if(!$current_user->exists()){
			$output['message_terminate']="Message: You are not logged in. Login first.";
			$handler->add_response_data(true, $output);
		}else{
		    $url = getMapUrl($form_name, $defaultTimezone);
            $response = json_decode(callAPI('GET', $url, false), true);
			if($response['success'] == "1"){
			    header('Location: http://www.example.com/'); // redirecting to map page
			    exit;
			}else{
                exit;
			}
			$handler->add_response_data(true, $output);
		}
	}
}, 10, 2 );



?>